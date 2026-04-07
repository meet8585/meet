"""Claude-powered agentic Metro 2 validation interface.

The agent accepts natural language questions and furnisher data in any format,
interprets the data, runs Metro 2 compliance validation, and explains the
results in plain English using tool use.
"""

from __future__ import annotations

import json
import os
from typing import Any

import anthropic

from .parser import Metro2Parser
from .validator import Metro2Validator
from .report import ValidationReport
from .constants import (
    ACCOUNT_STATUS_CODES,
    ACCOUNT_TYPES,
    ECOA_CODES,
    PAYMENT_RATING_CODES,
    PORTFOLIO_TYPES,
    TERMS_FREQUENCY_CODES,
)

_client = anthropic.Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))
_parser = Metro2Parser()
_validator = Metro2Validator()

SYSTEM_PROMPT = """You are an expert Metro 2 credit reporting compliance specialist.
Metro 2 is the standard format used by data furnishers (banks, lenders, creditors) to
report consumer account information to the major credit bureaus (Equifax, Experian,
TransUnion, Innovis).

Your job is to:
1. Accept credit account data in any format (JSON, CSV, fixed-width Metro 2, or natural language)
2. Validate whether each record is Metro 2 compliant
3. Explain every compliance violation clearly
4. Provide actionable guidance on how to fix issues
5. Answer questions about Metro 2 requirements

When the user provides data:
- Use the `validate_records` tool to run compliance checks
- Use the `lookup_metro2_code` tool to look up valid Metro 2 codes
- Use the `explain_metro2_rule` tool to explain specific rules
- Summarize findings in plain English after calling tools

Important Metro 2 rules you enforce:
- All dates must be in MMDDYYYY format and be valid calendar dates
- FCRA compliance/first delinquency dates are REQUIRED for delinquent/charged-off accounts
- Account status and payment rating must be compatible
- SSNs must be 9 digits with no dashes
- ECOA codes, portfolio types, account statuses, and payment ratings must use valid codes
- Amount past due should be non-zero for past-due account statuses (71, 78, 80, 82, 83, 84)
- Dates cannot be in the future
- Date of account information cannot precede date opened

Always be specific about which fields violate which rules and cite the rule code."""

TOOLS = [
    {
        "name": "validate_records",
        "description": (
            "Validate one or more Metro 2 account records for compliance. "
            "Accepts JSON (single record dict or list of dicts), CSV string, "
            "or Metro 2 fixed-width format string. "
            "Returns a detailed validation report with all errors and warnings."
        ),
        "input_schema": {
            "type": "object",
            "properties": {
                "data": {
                    "type": "string",
                    "description": (
                        "The account data to validate. Can be: "
                        "(1) JSON string — single record {field: value} or array of records, "
                        "(2) CSV string with header row, "
                        "(3) Metro 2 fixed-width 426-char record string. "
                        "Field names can use common aliases (e.g. 'ssn', 'last_name', 'status')."
                    ),
                },
                "format": {
                    "type": "string",
                    "enum": ["auto", "json", "csv", "fixed_width"],
                    "description": "Input format (default: auto-detect)",
                },
            },
            "required": ["data"],
        },
    },
    {
        "name": "lookup_metro2_code",
        "description": "Look up valid Metro 2 codes for a specific field.",
        "input_schema": {
            "type": "object",
            "properties": {
                "field": {
                    "type": "string",
                    "enum": [
                        "account_status",
                        "payment_rating",
                        "portfolio_type",
                        "account_type",
                        "ecoa_code",
                        "terms_frequency",
                    ],
                    "description": "The Metro 2 field to look up valid codes for.",
                },
            },
            "required": ["field"],
        },
    },
    {
        "name": "explain_metro2_rule",
        "description": "Explain a Metro 2 compliance rule by its rule code or field name.",
        "input_schema": {
            "type": "object",
            "properties": {
                "rule_or_field": {
                    "type": "string",
                    "description": (
                        "A rule code (e.g. 'FCRA-001', 'PR-003') or field name "
                        "(e.g. 'payment_rating', 'fcra_compliance_date')."
                    ),
                },
            },
            "required": ["rule_or_field"],
        },
    },
]

RULE_EXPLANATIONS = {
    "RDW-001": "Record Descriptor Word must be '0426' for all Metro 2 base segment records.",
    "PI-001": "Processing Indicator must be blank, '1' (normal), '2', or 'D' (Delete Account).",
    "ACCT-001": "Account Number is a required field; it identifies the account being reported.",
    "ACCT-002": "Account Number cannot exceed 20 characters in the Metro 2 fixed-width format.",
    "PORT-001": "Portfolio Type is required. It classifies the account type at a high level.",
    "PORT-002": (
        "Portfolio Type must be C (Credit Card), I (Installment), M (Mortgage), "
        "O (Open Account), or R (Revolving)."
    ),
    "AT-001": "Account Type must be a valid 2-digit code from the Metro 2 specification (00-99).",
    "DATE-001": "Date Opened is required and cannot be zero-filled or blank.",
    "DATE-002": "Date Opened must be in MMDDYYYY format (e.g., 01152020 for January 15, 2020).",
    "DATE-003": "Date Opened cannot be a future date.",
    "DATE-004": "Date Opened year must be 1900 or later.",
    "STATUS-001": "Account Status is required.",
    "STATUS-002": (
        "Account Status must be a valid Metro 2 code. Common codes: "
        "11=Current, 71-84=Delinquent, 93=Charge-off, 94=Repossession."
    ),
    "PR-001": "Payment Rating is required.",
    "PR-002": "Payment Rating must be a valid code: 0-6, B, D, E, or G.",
    "PR-003": (
        "Payment Rating must be compatible with Account Status. "
        "For example, status 71 (30-59 days past due) requires payment rating '1'."
    ),
    "PHP-001": (
        "Payment History Profile codes must be from the valid set: "
        "0-6 (delinquency levels), B (no history), D (no payment received), "
        "E (zero balance current), G (collection/charge-off), H, J, K, U, or space."
    ),
    "BAL-001": "Current Balance must be numeric, right-justified, zero-filled.",
    "APD-001": "Amount Past Due must be numeric.",
    "APD-002": (
        "When account status indicates a past-due condition (71, 78, 80, 82, 83, 84), "
        "the Amount Past Due should reflect the actual past-due amount."
    ),
    "DAI-001": "Date of Account Information (the 'as-of' date) is required.",
    "DAI-002": "Date of Account Information must be in MMDDYYYY format.",
    "DAI-003": "Date of Account Information cannot be in the future.",
    "DAI-004": "Date of Account Information cannot be before the Date Opened.",
    "FCRA-001": (
        "FCRA Compliance Date (first delinquency date) is REQUIRED when the account "
        "status code indicates a delinquent, charged-off, repossessed, or bankrupt "
        "condition (e.g., status codes 71, 78, 80-84, 90-97). "
        "This date establishes the 7-year credit reporting clock under the FCRA."
    ),
    "FCRA-002": "FCRA Compliance Date cannot be before the Date Opened.",
    "FCRA-003": "FCRA Compliance Date cannot be in the future.",
    "FCRA-004": "FCRA Compliance Date must be in MMDDYYYY format or 00000000 if not applicable.",
    "DC-001": "Date Closed must be in MMDDYYYY format.",
    "DC-002": "Date Closed cannot be before Date Opened.",
    "DC-003": "Date Closed cannot be in the future.",
    "DC-004": (
        "Closed account status codes (13, 62, 63, 64, 65, 05) should include a "
        "Date Closed to accurately reflect when the account was closed."
    ),
    "DLP-001": "Date of Last Payment must be in MMDDYYYY format.",
    "DLP-002": "Date of Last Payment cannot be before Date Opened.",
    "DLP-003": "Date of Last Payment cannot be in the future.",
    "SSN-001": "Social Security Number must be exactly 9 numeric digits with no dashes.",
    "SSN-002": "The provided SSN appears to be invalid (all same digits or sequential).",
    "NAME-001": "Consumer surname or first name is required.",
    "NAME-002": "Consumer surname cannot exceed 25 characters.",
    "NAME-003": "Consumer first name cannot exceed 20 characters.",
    "ECOA-001": "ECOA Code is required. It indicates the consumer's credit relationship.",
    "ECOA-002": (
        "ECOA Code must be valid: 1=Individual, 2=Joint, 3=Undesignated, "
        "4=Joint User, 5=Co-maker, 6=On behalf, 7=Maker, 8=Deceased, "
        "9=Sign only, B=Business, T=Terminated, W=Commercial, X=Deceased joint, Z=Delete."
    ),
    "CO-001": "Charge-off status codes (93, 97) should have a non-zero Original Charge-off Amount.",
    "CO-002": "Original Charge-off Amount must be numeric.",
    "TF-001": (
        "Terms Frequency must be a valid code: D=Deferred, W=Weekly, B=Biweekly, "
        "S=Semimonthly, M=Monthly, L=Bimonthly, P=Quarterly, Y=Annual, "
        "1=Single Payment, 2=Unknown, 3=Irregular, X=Not Reported."
    ),
}


# ── Tool execution ─────────────────────────────────────────────────────────────

def _execute_tool(name: str, tool_input: dict) -> str:
    if name == "validate_records":
        return _tool_validate_records(tool_input)
    elif name == "lookup_metro2_code":
        return _tool_lookup_code(tool_input)
    elif name == "explain_metro2_rule":
        return _tool_explain_rule(tool_input)
    return json.dumps({"error": f"Unknown tool: {name}"})


def _tool_validate_records(tool_input: dict) -> str:
    data = tool_input.get("data", "")
    fmt = tool_input.get("format", "auto")

    try:
        if fmt == "json":
            records = _parser.parse_json(data)
        elif fmt == "csv":
            records = _parser.parse_csv(data)
        elif fmt == "fixed_width":
            records = _parser.parse_fixed_width_string(data)
        else:
            records = _parser.parse_auto(data)

        if not records:
            return json.dumps({"error": "No records found in the provided data."})

        results = _validator.validate_records(records)
        report = ValidationReport(results)
        return report.to_json()

    except Exception as exc:
        return json.dumps({"error": f"Failed to parse/validate data: {exc}"})


def _tool_lookup_code(tool_input: dict) -> str:
    field = tool_input.get("field", "")
    mapping = {
        "account_status": ACCOUNT_STATUS_CODES,
        "payment_rating": PAYMENT_RATING_CODES,
        "portfolio_type": PORTFOLIO_TYPES,
        "account_type": ACCOUNT_TYPES,
        "ecoa_code": ECOA_CODES,
        "terms_frequency": TERMS_FREQUENCY_CODES,
    }
    codes = mapping.get(field)
    if codes is None:
        return json.dumps({"error": f"Unknown field '{field}'"})
    return json.dumps({field: codes}, indent=2)


def _tool_explain_rule(tool_input: dict) -> str:
    key = tool_input.get("rule_or_field", "")
    if key in RULE_EXPLANATIONS:
        return json.dumps({"rule": key, "explanation": RULE_EXPLANATIONS[key]})

    # Search by field name prefix
    matches = {k: v for k, v in RULE_EXPLANATIONS.items()
               if key.upper() in k.upper() or key.lower() in v.lower()}
    if matches:
        return json.dumps({"matches": matches}, indent=2)

    return json.dumps({"error": f"No explanation found for '{key}'"})


# ── Agent loop ─────────────────────────────────────────────────────────────────

class Metro2Agent:
    """
    Claude-powered Metro 2 validation agent.

    Usage:
        agent = Metro2Agent()
        response = agent.chat("Validate this record: {...}")
        print(response)
    """

    def __init__(self, model: str = "claude-opus-4-6"):
        self.model = model
        self.messages: list[dict] = []

    def chat(self, user_message: str) -> str:
        """Send a message and get a Metro 2 compliance response."""
        self.messages.append({"role": "user", "content": user_message})

        while True:
            response = _client.messages.create(
                model=self.model,
                max_tokens=16000,
                thinking={"type": "adaptive"},
                system=SYSTEM_PROMPT,
                tools=TOOLS,
                messages=self.messages,
            )

            # Collect text and tool-use blocks
            text_parts: list[str] = []
            tool_use_blocks: list[dict] = []

            for block in response.content:
                if block.type == "text":
                    text_parts.append(block.text)
                elif block.type == "tool_use":
                    tool_use_blocks.append({
                        "id": block.id,
                        "name": block.name,
                        "input": block.input,
                    })

            # Append assistant message
            self.messages.append({"role": "assistant", "content": response.content})

            # If no tool calls, we're done
            if response.stop_reason == "end_turn" or not tool_use_blocks:
                return "\n".join(text_parts).strip()

            # Execute tools and collect results
            tool_results = []
            for tb in tool_use_blocks:
                result_content = _execute_tool(tb["name"], tb["input"])
                tool_results.append({
                    "type": "tool_result",
                    "tool_use_id": tb["id"],
                    "content": result_content,
                })

            self.messages.append({"role": "user", "content": tool_results})

    def reset(self):
        """Clear conversation history."""
        self.messages = []

    def validate_and_explain(self, data: str | dict | list, fmt: str = "auto") -> str:
        """
        Shortcut: validate data and return a natural-language explanation.

        Args:
            data: Account data (JSON string, dict, list of dicts, CSV, or fixed-width)
            fmt:  'auto' | 'json' | 'csv' | 'fixed_width'
        """
        if isinstance(data, (dict, list)):
            import json
            data_str = json.dumps(data)
            fmt = "json"
        else:
            data_str = data

        prompt = (
            f"Please validate the following Metro 2 credit reporting data and provide "
            f"a detailed compliance analysis. For each violation, explain what is wrong, "
            f"why it matters, and how to fix it.\n\n"
            f"Data format: {fmt}\n\n"
            f"```\n{data_str}\n```"
        )
        return self.chat(prompt)
