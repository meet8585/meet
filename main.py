#!/usr/bin/env python3
"""Metro 2 Compliance Validation Tool — CLI entry point."""

import json
import sys
from pathlib import Path

import click

from metro2_validator.parser import Metro2Parser
from metro2_validator.validator import Metro2Validator
from metro2_validator.report import ValidationReport


@click.group()
def cli():
    """Metro 2 Credit Reporting Compliance Validator."""
    pass


# ── validate command ───────────────────────────────────────────────────────────

@cli.command()
@click.argument("input", type=click.Path(exists=True), required=False)
@click.option("--data", "-d", default=None,
              help="Inline data string (JSON, CSV, or Metro 2 fixed-width)")
@click.option("--format", "-f", "fmt",
              type=click.Choice(["auto", "json", "csv", "fixed_width"]),
              default="auto", show_default=True,
              help="Input format (auto-detected by default)")
@click.option("--output", "-o",
              type=click.Choice(["text", "json", "rich"]),
              default="rich", show_default=True,
              help="Output format")
@click.option("--output-file", type=click.Path(), default=None,
              help="Write output to file instead of stdout")
def validate(input, data, fmt, output, output_file):
    """Validate Metro 2 account records from a file or inline data.

    \b
    Examples:
      python main.py validate sample_data/sample.json
      python main.py validate --data '{"account_number":"12345","portfolio_type":"I",...}'
      python main.py validate records.csv --format csv --output json
    """
    parser = Metro2Parser()
    validator = Metro2Validator()

    # Load input
    if input:
        path = Path(input)
        suffix = path.suffix.lower()
        if suffix == ".json":
            records = parser.parse_json(path.read_text())
        elif suffix in (".csv", ".tsv"):
            records = parser.parse_csv_file(path, delimiter="\t" if suffix == ".tsv" else ",")
        else:
            records = parser.parse_fixed_width_file(path)
    elif data:
        if fmt == "json":
            records = parser.parse_json(data)
        elif fmt == "csv":
            records = parser.parse_csv(data)
        elif fmt == "fixed_width":
            records = parser.parse_fixed_width_string(data)
        else:
            records = parser.parse_auto(data)
    else:
        click.echo("Error: provide a file path or --data string.", err=True)
        sys.exit(1)

    if not records:
        click.echo("No records found.", err=True)
        sys.exit(1)

    # Validate
    results = validator.validate_records(records)
    report = ValidationReport(results)

    # Output
    if output == "json":
        text = report.to_json()
        if output_file:
            Path(output_file).write_text(text)
        else:
            click.echo(text)
    elif output == "text":
        text = report.to_text()
        if output_file:
            Path(output_file).write_text(text)
        else:
            click.echo(text)
    else:  # rich
        if output_file:
            click.echo(report.to_text())
            Path(output_file).write_text(report.to_text())
        else:
            report.print_rich()

    # Exit with non-zero if non-compliant
    sys.exit(0 if report.is_fully_compliant else 1)


# ── agent command ──────────────────────────────────────────────────────────────

@cli.command()
@click.option("--model", default="claude-opus-4-6", show_default=True,
              help="Claude model to use")
def agent(model):
    """Launch an interactive Metro 2 compliance agent (requires ANTHROPIC_API_KEY).

    \b
    The agent understands natural language. You can:
      - Paste account data in any format and ask for validation
      - Ask about specific Metro 2 rules
      - Look up valid code values
      - Get fix suggestions for compliance issues
    """
    try:
        from metro2_validator.agent import Metro2Agent
    except ImportError as e:
        click.echo(f"Agent unavailable: {e}", err=True)
        sys.exit(1)

    import os
    if not os.environ.get("ANTHROPIC_API_KEY"):
        click.echo(
            "Error: ANTHROPIC_API_KEY environment variable is not set.\n"
            "  export ANTHROPIC_API_KEY=your-key-here",
            err=True,
        )
        sys.exit(1)

    ag = Metro2Agent(model=model)

    try:
        from rich.console import Console
        console = Console()
        console.rule("[bold cyan]Metro 2 Compliance Agent[/]")
        console.print("[dim]Type your message or paste data. Enter 'quit' to exit, 'reset' to clear history.[/]")
        console.print()
    except ImportError:
        click.echo("=== Metro 2 Compliance Agent ===")
        click.echo("Type your message or paste data. Enter 'quit' to exit, 'reset' to clear.")
        click.echo()

    while True:
        try:
            user_input = click.prompt("You", prompt_suffix="> ")
        except (click.Abort, EOFError):
            click.echo("\nGoodbye.")
            break

        if user_input.strip().lower() in ("quit", "exit", "q"):
            click.echo("Goodbye.")
            break
        if user_input.strip().lower() == "reset":
            ag.reset()
            click.echo("[History cleared]")
            continue
        if not user_input.strip():
            continue

        try:
            response = ag.chat(user_input)
            click.echo()
            try:
                from rich.console import Console
                from rich.markdown import Markdown
                Console().print(Markdown(response))
            except ImportError:
                click.echo(response)
            click.echo()
        except Exception as exc:
            click.echo(f"[Agent error] {exc}", err=True)


# ── codes command ──────────────────────────────────────────────────────────────

@cli.command()
@click.argument("field", type=click.Choice([
    "account_status", "payment_rating", "portfolio_type",
    "account_type", "ecoa_code", "terms_frequency",
]))
def codes(field):
    """List valid Metro 2 codes for a field.

    \b
    Examples:
      python main.py codes account_status
      python main.py codes ecoa_code
    """
    from metro2_validator.constants import (
        ACCOUNT_STATUS_CODES, PAYMENT_RATING_CODES, PORTFOLIO_TYPES,
        ACCOUNT_TYPES, ECOA_CODES, TERMS_FREQUENCY_CODES,
    )
    mapping = {
        "account_status": ACCOUNT_STATUS_CODES,
        "payment_rating": PAYMENT_RATING_CODES,
        "portfolio_type": PORTFOLIO_TYPES,
        "account_type": ACCOUNT_TYPES,
        "ecoa_code": ECOA_CODES,
        "terms_frequency": TERMS_FREQUENCY_CODES,
    }
    codes_dict = mapping[field]
    click.echo(f"\nValid codes for '{field}':\n")
    for code, desc in codes_dict.items():
        click.echo(f"  {code:5s} — {desc}")
    click.echo()


# ── demo command ───────────────────────────────────────────────────────────────

@cli.command()
def demo():
    """Run a built-in demonstration with sample valid and invalid records."""
    from metro2_validator.parser import Metro2Parser
    from metro2_validator.validator import Metro2Validator
    from metro2_validator.report import ValidationReport

    parser = Metro2Parser()
    validator = Metro2Validator()

    sample_records = [
        # ── Record 1: Valid installment account ────────────────────────────
        {
            "account_number": "ACC123456789",
            "portfolio_type": "I",
            "account_type": "00",
            "date_opened": "01152015",
            "credit_limit": "025000",
            "terms_duration": "060",
            "terms_frequency": "M",
            "scheduled_monthly_payment_amount": "000450",
            "actual_payment_amount": "000450",
            "account_status": "11",
            "payment_rating": "0",
            "payment_history_profile": "000000000000000000000000",
            "current_balance": "012500",
            "amount_past_due": "000000",
            "date_of_account_information": "03012024",
            "ecoa_code": "1",
            "consumer_name_surname": "SMITH",
            "consumer_name_first": "JOHN",
            "date_of_birth": "06151985",
            "social_security_number": "123456789",
            "first_line_of_address": "123 MAIN ST",
            "city": "ANYTOWN",
            "state": "CA",
            "postal_code": "90210",
            "address_indicator": "C",
        },
        # ── Record 2: Delinquent — missing FCRA compliance date ────────────
        {
            "account_number": "BADACCT001",
            "portfolio_type": "R",
            "account_type": "20",
            "date_opened": "03102018",
            "terms_frequency": "M",
            "account_status": "71",       # 30-59 days past due
            "payment_rating": "1",
            "payment_history_profile": "100000000000000000000000",
            "current_balance": "003500",
            "amount_past_due": "000000",  # ERROR: should be non-zero
            # fcra_compliance_date missing — ERROR: required for status 71
            "date_of_account_information": "03012024",
            "ecoa_code": "2",
            "consumer_name_surname": "DOE",
            "consumer_name_first": "JANE",
            "state": "ZZ",               # WARNING: invalid state
        },
        # ── Record 3: Charge-off — multiple issues ─────────────────────────
        {
            "account_number": "CHARGEOFF002",
            "portfolio_type": "C",
            "account_type": "20",
            "date_opened": "07202020",
            "terms_frequency": "M",
            "account_status": "97",       # Unpaid balance / loss
            "payment_rating": "0",        # ERROR: should be G for status 97
            "payment_history_profile": "6666G44444333322110000 X",  # invalid 'X'
            "current_balance": "004200",
            "amount_past_due": "004200",
            "original_charge_off_amount": "000000",  # WARNING: should be non-zero
            "date_of_account_information": "03012024",
            "fcra_compliance_date": "06012021",
            "ecoa_code": "9",             # WARNING: valid but unusual for this type
            "consumer_name_surname": "JOHNSON",
            "consumer_name_first": "ROBERT",
            "date_of_birth": "13201990",  # ERROR: invalid date (month 13)
            "social_security_number": "000000000",  # ERROR: all zeros
        },
    ]

    results = validator.validate_records(sample_records)
    report = ValidationReport(results)
    report.print_rich()


if __name__ == "__main__":
    cli()
