"""Validation report formatter — plain text, JSON, and Rich console output."""

from __future__ import annotations

import json
from dataclasses import asdict
from typing import Any

from .validator import ValidationResult, ValidationError


class ValidationReport:
    """Aggregate and format validation results."""

    def __init__(self, results: list[ValidationResult]):
        self.results = results

    # ── Aggregate stats ────────────────────────────────────────────────────────

    @property
    def total_records(self) -> int:
        return len(self.results)

    @property
    def valid_count(self) -> int:
        return sum(1 for r in self.results if r.is_valid)

    @property
    def invalid_count(self) -> int:
        return self.total_records - self.valid_count

    @property
    def total_errors(self) -> int:
        return sum(r.error_count for r in self.results)

    @property
    def total_warnings(self) -> int:
        return sum(r.warning_count for r in self.results)

    @property
    def is_fully_compliant(self) -> bool:
        return self.total_errors == 0

    # ── Summary dict ──────────────────────────────────────────────────────────

    def to_dict(self) -> dict[str, Any]:
        return {
            "summary": {
                "total_records": self.total_records,
                "valid_records": self.valid_count,
                "invalid_records": self.invalid_count,
                "total_errors": self.total_errors,
                "total_warnings": self.total_warnings,
                "compliant": self.is_fully_compliant,
            },
            "records": [
                {
                    "index": r.record_index,
                    "account_number": r.account_number,
                    "valid": r.is_valid,
                    "errors": [
                        {
                            "field": e.field_name,
                            "value": e.value,
                            "message": e.message,
                            "rule": e.rule,
                            "severity": e.severity,
                        }
                        for e in r.errors
                    ],
                    "warnings": [
                        {
                            "field": e.field_name,
                            "value": e.value,
                            "message": e.message,
                            "rule": e.rule,
                            "severity": e.severity,
                        }
                        for e in r.warnings
                    ],
                }
                for r in self.results
            ],
        }

    def to_json(self, indent: int = 2) -> str:
        return json.dumps(self.to_dict(), indent=indent)

    # ── Plain text ─────────────────────────────────────────────────────────────

    def to_text(self) -> str:
        lines: list[str] = []
        lines.append("=" * 72)
        lines.append("  METRO 2 COMPLIANCE VALIDATION REPORT")
        lines.append("=" * 72)
        lines.append(f"  Total Records   : {self.total_records}")
        lines.append(f"  Valid Records   : {self.valid_count}")
        lines.append(f"  Invalid Records : {self.invalid_count}")
        lines.append(f"  Total Errors    : {self.total_errors}")
        lines.append(f"  Total Warnings  : {self.total_warnings}")
        verdict = "COMPLIANT" if self.is_fully_compliant else "NON-COMPLIANT"
        lines.append(f"  Overall Status  : {verdict}")
        lines.append("=" * 72)
        lines.append("")

        for r in self.results:
            acct = r.account_number or f"Record #{r.record_index + 1}"
            status = "✓ VALID" if r.is_valid else f"✗ INVALID ({r.error_count} error(s))"
            lines.append(f"  Account: {acct}  [{status}]")

            if r.errors:
                for e in r.errors:
                    lines.append(f"    [ERROR][{e.rule}] {e.field_name}: {e.message}")
                    if e.value:
                        lines.append(f"           Value: '{e.value}'")

            if r.warnings:
                for w in r.warnings:
                    lines.append(f"    [WARN] [{w.rule}] {w.field_name}: {w.message}")
                    if w.value:
                        lines.append(f"           Value: '{w.value}'")

            if r.is_valid and not r.warnings:
                lines.append("    All checks passed.")
            lines.append("")

        return "\n".join(lines)

    # ── Rich console (optional) ────────────────────────────────────────────────

    def print_rich(self):
        """Print a colorized report using the Rich library (if available)."""
        try:
            from rich.console import Console
            from rich.table import Table
            from rich import box
            from rich.text import Text
        except ImportError:
            print(self.to_text())
            return

        console = Console()
        console.print()
        console.rule("[bold cyan]Metro 2 Compliance Validation Report[/]")

        # Summary table
        summary = Table(box=box.ROUNDED, show_header=False, padding=(0, 2))
        summary.add_column("Field", style="bold")
        summary.add_column("Value")
        summary.add_row("Total Records", str(self.total_records))
        summary.add_row("Valid Records", f"[green]{self.valid_count}[/]")
        summary.add_row("Invalid Records",
                        f"[red]{self.invalid_count}[/]" if self.invalid_count else "[green]0[/]")
        summary.add_row("Total Errors",
                        f"[red]{self.total_errors}[/]" if self.total_errors else "[green]0[/]")
        summary.add_row("Total Warnings",
                        f"[yellow]{self.total_warnings}[/]" if self.total_warnings else "[green]0[/]")
        verdict = "[bold green]COMPLIANT[/]" if self.is_fully_compliant else "[bold red]NON-COMPLIANT[/]"
        summary.add_row("Overall Status", verdict)
        console.print(summary)
        console.print()

        # Per-record details
        for r in self.results:
            acct = r.account_number or f"Record #{r.record_index + 1}"
            if r.is_valid and not r.warnings:
                console.print(f"  [green]✓[/] [bold]{acct}[/] — all checks passed")
            else:
                icon = "[red]✗[/]" if not r.is_valid else "[yellow]⚠[/]"
                console.print(f"  {icon} [bold]{acct}[/]")

                for e in r.errors:
                    console.print(
                        f"    [red][ERROR][/] [[dim]{e.rule}[/]] "
                        f"[cyan]{e.field_name}[/]: {e.message}"
                    )
                    if e.value and e.field_name != "social_security_number":
                        console.print(f"           [dim]Value:[/] '{e.value}'")

                for w in r.warnings:
                    console.print(
                        f"    [yellow][WARN][/]  [[dim]{w.rule}[/]] "
                        f"[cyan]{w.field_name}[/]: {w.message}"
                    )
                    if w.value:
                        console.print(f"           [dim]Value:[/] '{w.value}'")
            console.print()
