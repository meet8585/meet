"""Metro 2 File and JSON Parser — converts raw data into dict records."""

from __future__ import annotations

import csv
import io
import json
from pathlib import Path
from typing import Any

from .validator import ValidationResult
from .fields import BASE_SEGMENT_FIELDS


class Metro2Parser:
    """Parse Metro 2 data from multiple formats."""

    # ── Fixed-Width Format ─────────────────────────────────────────────────────

    def parse_fixed_width_file(self, path: str | Path) -> list[dict[str, Any]]:
        """Parse a Metro 2 fixed-width text file into a list of record dicts."""
        records = []
        with open(path, "r", encoding="latin-1") as fh:
            for line in fh:
                line = line.rstrip("\n\r")
                if not line.strip():
                    continue
                rec = self._parse_fixed_width_line(line)
                if rec:
                    records.append(rec)
        return records

    def parse_fixed_width_string(self, content: str) -> list[dict[str, Any]]:
        """Parse a multi-line fixed-width Metro 2 string."""
        records = []
        for line in content.splitlines():
            line = line.rstrip()
            if not line.strip():
                continue
            rec = self._parse_fixed_width_line(line)
            if rec:
                records.append(rec)
        return records

    def _parse_fixed_width_line(self, line: str) -> dict[str, Any] | None:
        """Extract fields from one 426-char record line."""
        if len(line) < 4:
            return None
        result: dict[str, Any] = {"_raw": line}
        for fd in BASE_SEGMENT_FIELDS:
            if fd.end <= len(line):
                result[fd.name] = fd.extract(line).rstrip()
        return result

    # ── JSON Format ────────────────────────────────────────────────────────────

    def parse_json(self, data: str | dict | list) -> list[dict[str, Any]]:
        """
        Parse account records from JSON.

        Accepts:
        - A JSON string (single object or array)
        - A Python dict (single record)
        - A Python list of dicts
        """
        if isinstance(data, str):
            parsed = json.loads(data)
        else:
            parsed = data

        if isinstance(parsed, dict):
            return [self._normalize(parsed)]
        elif isinstance(parsed, list):
            return [self._normalize(r) for r in parsed]
        else:
            raise ValueError(f"Unsupported JSON structure: {type(parsed)}")

    def _normalize(self, record: dict) -> dict[str, Any]:
        """Normalize field names to snake_case Metro 2 field names."""
        aliases = {
            # Human-readable aliases → canonical Metro 2 field names
            "acct_number": "account_number",
            "acct_no": "account_number",
            "portfolio": "portfolio_type",
            "type": "account_type",
            "opened": "date_opened",
            "open_date": "date_opened",
            "status": "account_status",
            "balance": "current_balance",
            "current_balance_amount": "current_balance",
            "past_due": "amount_past_due",
            "past_due_amount": "amount_past_due",
            "charge_off": "original_charge_off_amount",
            "info_date": "date_of_account_information",
            "as_of_date": "date_of_account_information",
            "first_delinquency_date": "fcra_compliance_date",
            "delinquency_date": "fcra_compliance_date",
            "closed_date": "date_closed",
            "last_payment_date": "date_of_last_payment",
            "ssn": "social_security_number",
            "surname": "consumer_name_surname",
            "last_name": "consumer_name_surname",
            "first_name": "consumer_name_first",
            "middle_name": "consumer_name_middle",
            "dob": "date_of_birth",
            "birth_date": "date_of_birth",
            "phone": "telephone_number",
            "ecoa": "ecoa_code",
            "payment_history": "payment_history_profile",
            "history": "payment_history_profile",
            "address_line_1": "first_line_of_address",
            "address_line_2": "second_line_of_address",
            "address1": "first_line_of_address",
            "address2": "second_line_of_address",
            "zip": "postal_code",
            "zip_code": "postal_code",
        }
        normalized: dict[str, Any] = {}
        for k, v in record.items():
            key = k.lower().strip().replace("-", "_").replace(" ", "_")
            key = aliases.get(key, key)
            normalized[key] = v
        return normalized

    # ── CSV Format ─────────────────────────────────────────────────────────────

    def parse_csv(self, data: str, delimiter: str = ",") -> list[dict[str, Any]]:
        """Parse account records from a CSV string."""
        reader = csv.DictReader(io.StringIO(data), delimiter=delimiter)
        records = []
        for row in reader:
            records.append(self._normalize(dict(row)))
        return records

    def parse_csv_file(self, path: str | Path, delimiter: str = ",") -> list[dict[str, Any]]:
        """Parse account records from a CSV file."""
        with open(path, "r", encoding="utf-8-sig") as fh:
            return self.parse_csv(fh.read(), delimiter=delimiter)

    # ── Auto-detect Format ─────────────────────────────────────────────────────

    def parse_auto(self, data: str) -> list[dict[str, Any]]:
        """
        Auto-detect format and parse.

        - Starts with '{' or '[' → JSON
        - Contains commas and header row → CSV
        - 426+ chars per line → fixed-width Metro 2
        """
        stripped = data.strip()
        if stripped.startswith("{") or stripped.startswith("["):
            return self.parse_json(stripped)

        lines = [l for l in stripped.splitlines() if l.strip()]
        if not lines:
            return []

        # Heuristic: if first line ≥ 354 chars and is mostly printable ASCII
        if len(lines[0]) >= 354:
            return self.parse_fixed_width_string(data)

        # Try CSV
        if "," in lines[0] or "\t" in lines[0]:
            delim = "\t" if "\t" in lines[0] else ","
            return self.parse_csv(data, delim)

        # Fallback: try fixed-width anyway
        return self.parse_fixed_width_string(data)
