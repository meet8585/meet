"""Metro 2 Compliance Validator — field-level and cross-field rules."""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from datetime import date, datetime
from typing import Any, Optional

from .constants import (
    ACCOUNT_STATUS_CODES,
    ACCOUNT_TYPES,
    ADDRESS_INDICATOR_CODES,
    COMPLIANCE_CONDITION_CODES,
    CONSUMER_INFO_INDICATORS,
    DELINQUENCY_STATUS_CODES,
    ECOA_CODES,
    GENERATION_CODES,
    INTEREST_TYPE_INDICATORS,
    PAYMENT_HISTORY_CODES,
    PAYMENT_RATING_CODES,
    PORTFOLIO_TYPES,
    RECORD_DESCRIPTOR_WORD,
    RESIDENCE_CODES,
    SPECIAL_COMMENT_CODES,
    STATUS_PAYMENT_RATING_MAP,
    TERMS_FREQUENCY_CODES,
    US_STATE_CODES,
)


# ── Result types ───────────────────────────────────────────────────────────────

@dataclass
class ValidationError:
    field_name: str
    value: str
    message: str
    severity: str = "ERROR"    # ERROR | WARNING | INFO
    rule: str = ""


@dataclass
class ValidationResult:
    record_index: int
    record_type: str           # "HEADER" | "BASE" | "TRAILER"
    account_number: str = ""
    errors: list[ValidationError] = field(default_factory=list)
    warnings: list[ValidationError] = field(default_factory=list)

    @property
    def is_valid(self) -> bool:
        return len(self.errors) == 0

    @property
    def error_count(self) -> int:
        return len(self.errors)

    @property
    def warning_count(self) -> int:
        return len(self.warnings)

    def add_error(self, field_name: str, value: str, message: str, rule: str = ""):
        self.errors.append(ValidationError(field_name, value, message, "ERROR", rule))

    def add_warning(self, field_name: str, value: str, message: str, rule: str = ""):
        self.warnings.append(ValidationError(field_name, value, message, "WARNING", rule))


# ── Helpers ────────────────────────────────────────────────────────────────────

def _parse_date(value: str) -> Optional[date]:
    """Parse MMDDYYYY → date, return None on failure."""
    value = value.strip()
    if value in ("00000000", "        ", ""):
        return None
    try:
        return datetime.strptime(value, "%m%d%Y").date()
    except ValueError:
        return None


def _is_zero_filled_date(value: str) -> bool:
    return value.strip() in ("00000000", "")


def _is_numeric(value: str) -> bool:
    return value.strip().replace(" ", "").isdigit() or value.strip() == ""


def _is_alphanumeric(value: str) -> bool:
    return all(c.isalnum() or c in " -.,'#/" for c in value)


def _all_zeros(value: str) -> bool:
    return value.strip() == "" or all(c in "0 " for c in value)


def _strip_right(value: str) -> str:
    return value.rstrip()


# ── Field Validators ───────────────────────────────────────────────────────────

class Metro2Validator:
    """
    Validate Metro 2 account records.

    Accepts either:
    - dict records (from JSON / parsed data)
    - raw 426-character fixed-width strings
    """

    def validate_record(self, record: dict[str, Any], index: int = 0) -> ValidationResult:
        """Validate a single account record provided as a dict."""
        result = ValidationResult(
            record_index=index,
            record_type="BASE",
            account_number=str(record.get("account_number", "")).strip(),
        )
        self._validate_base_segment(record, result)
        return result

    def validate_records(self, records: list[dict[str, Any]]) -> list[ValidationResult]:
        """Validate a list of account records."""
        return [self.validate_record(r, i) for i, r in enumerate(records)]

    def validate_fixed_width(self, line: str, index: int = 0) -> ValidationResult:
        """Validate a raw 426-character Metro 2 base segment string."""
        if len(line) < 354:
            result = ValidationResult(index, "BASE")
            result.add_error("record_length", str(len(line)),
                             f"Record must be at least 354 characters; got {len(line)}",
                             "FORMAT-001")
            return result
        record = self._parse_fixed_width(line)
        return self.validate_record(record, index)

    # ── Internal ───────────────────────────────────────────────────────────────

    def _parse_fixed_width(self, line: str) -> dict[str, Any]:
        """Convert a fixed-width record string to a dict."""
        def f(start: int, length: int) -> str:
            return line[start - 1 : start - 1 + length]

        return {
            "record_descriptor_word":          f(1,  4),
            "processing_indicator":             f(5,  1),
            "account_number":                   f(6,  20),
            "portfolio_type":                   f(26, 1),
            "account_type":                     f(27, 2),
            "date_opened":                      f(29, 8),
            "credit_limit":                     f(37, 9),
            "terms_duration":                   f(46, 3),
            "terms_frequency":                  f(49, 1),
            "scheduled_monthly_payment_amount": f(50, 9),
            "actual_payment_amount":            f(59, 9),
            "account_status":                   f(68, 2),
            "payment_rating":                   f(70, 1),
            "payment_history_profile":          f(71, 24),
            "special_comment":                  f(95, 2),
            "compliance_condition_code":        f(97, 2),
            "current_balance":                  f(99, 9),
            "amount_past_due":                  f(108, 9),
            "original_charge_off_amount":       f(117, 9),
            "date_of_account_information":      f(126, 8),
            "fcra_compliance_date":             f(134, 8),
            "date_closed":                      f(142, 8),
            "date_of_last_payment":             f(150, 8),
            "interest_type_indicator":          f(158, 1),
            "social_security_number":           f(160, 9),
            "consumer_name_surname":            f(169, 25),
            "consumer_name_first":              f(194, 20),
            "consumer_name_middle":             f(214, 20),
            "generation_code":                  f(234, 1),
            "date_of_birth":                    f(235, 8),
            "telephone_number":                 f(243, 10),
            "ecoa_code":                        f(253, 1),
            "consumer_information_indicator":   f(254, 2),
            "country_code":                     f(256, 2),
            "first_line_of_address":            f(258, 32),
            "second_line_of_address":           f(290, 32),
            "city":                             f(322, 20),
            "state":                            f(342, 2),
            "postal_code":                      f(344, 9),
            "address_indicator":                f(353, 1),
            "residence_code":                   f(354, 1) if len(line) >= 354 else " ",
        }

    def _validate_base_segment(self, r: dict, result: ValidationResult):
        today = date.today()

        # ── 1. Record Descriptor Word ────────────────────────────────────────
        rdw = str(r.get("record_descriptor_word", "")).strip()
        if rdw and rdw != RECORD_DESCRIPTOR_WORD:
            result.add_error("record_descriptor_word", rdw,
                             f"Must be '{RECORD_DESCRIPTOR_WORD}'; got '{rdw}'",
                             "RDW-001")

        # ── 2. Processing Indicator ──────────────────────────────────────────
        pi = str(r.get("processing_indicator", "1")).strip()
        if pi not in ("", "1", "2", "D"):
            result.add_error("processing_indicator", pi,
                             f"Invalid value '{pi}'; must be blank, '1', '2', or 'D'",
                             "PI-001")

        # ── 3. Account Number ────────────────────────────────────────────────
        acct = str(r.get("account_number", "")).strip()
        if not acct:
            result.add_error("account_number", acct,
                             "Account number is required and cannot be blank",
                             "ACCT-001")
        elif len(acct) > 20:
            result.add_error("account_number", acct,
                             f"Account number exceeds 20 characters (got {len(acct)})",
                             "ACCT-002")

        # ── 4. Portfolio Type ────────────────────────────────────────────────
        pt = str(r.get("portfolio_type", "")).strip()
        if not pt:
            result.add_error("portfolio_type", pt,
                             "Portfolio type is required",
                             "PORT-001")
        elif pt not in PORTFOLIO_TYPES:
            result.add_error("portfolio_type", pt,
                             f"Invalid portfolio type '{pt}'; must be one of: "
                             f"{', '.join(PORTFOLIO_TYPES.keys())}",
                             "PORT-002")

        # ── 5. Account Type ──────────────────────────────────────────────────
        at = str(r.get("account_type", "")).strip().zfill(2)
        if not at or at == "00" and pt in ("I", "M", "R", "C"):
            # account type 00 is reserved for Auto; warn if unusual
            pass
        if at not in ACCOUNT_TYPES:
            result.add_error("account_type", at,
                             f"Invalid account type '{at}'; must be a valid 2-digit code (00-99)",
                             "AT-001")

        # ── 6. Date Opened ───────────────────────────────────────────────────
        do_raw = str(r.get("date_opened", "")).strip()
        date_opened = _parse_date(do_raw)
        if not do_raw or _is_zero_filled_date(do_raw):
            result.add_error("date_opened", do_raw,
                             "Date opened is required and cannot be zero-filled",
                             "DATE-001")
        elif date_opened is None:
            result.add_error("date_opened", do_raw,
                             f"Invalid date format '{do_raw}'; expected MMDDYYYY",
                             "DATE-002")
        elif date_opened > today:
            result.add_error("date_opened", do_raw,
                             "Date opened cannot be in the future",
                             "DATE-003")
        elif date_opened.year < 1900:
            result.add_error("date_opened", do_raw,
                             "Date opened year must be 1900 or later",
                             "DATE-004")

        # ── 7. Credit Limit ──────────────────────────────────────────────────
        cl_raw = str(r.get("credit_limit", "")).strip()
        if cl_raw and not cl_raw.replace("0", "").replace(" ", "") == "":
            if not re.fullmatch(r"\d+", cl_raw):
                result.add_error("credit_limit", cl_raw,
                                 "Credit limit must be numeric (right justified, zero filled)",
                                 "CL-001")
            elif int(cl_raw) < 0:
                result.add_error("credit_limit", cl_raw,
                                 "Credit limit cannot be negative",
                                 "CL-002")

        # ── 8. Terms Duration ────────────────────────────────────────────────
        td = str(r.get("terms_duration", "")).strip()
        if td and td not in ("LOC", "REV", "MIN", "   ", "000"):
            if not re.fullmatch(r"\d{1,3}", td):
                result.add_error("terms_duration", td,
                                 "Terms duration must be 001-999, 'LOC', 'REV', 'MIN', or blank",
                                 "TD-001")

        # ── 9. Terms Frequency ───────────────────────────────────────────────
        tf = str(r.get("terms_frequency", "")).strip()
        if tf and tf not in TERMS_FREQUENCY_CODES:
            result.add_error("terms_frequency", tf,
                             f"Invalid terms frequency '{tf}'; must be one of: "
                             f"{', '.join(TERMS_FREQUENCY_CODES.keys())}",
                             "TF-001")

        # ── 10. Account Status ───────────────────────────────────────────────
        status = str(r.get("account_status", "")).strip()
        if not status:
            result.add_error("account_status", status,
                             "Account status is required",
                             "STATUS-001")
        elif status not in ACCOUNT_STATUS_CODES:
            result.add_error("account_status", status,
                             f"Invalid account status '{status}'; must be one of: "
                             f"{', '.join(sorted(ACCOUNT_STATUS_CODES.keys()))}",
                             "STATUS-002")

        # ── 11. Payment Rating ───────────────────────────────────────────────
        pr = str(r.get("payment_rating", "")).strip()
        if not pr:
            result.add_error("payment_rating", pr,
                             "Payment rating is required",
                             "PR-001")
        elif pr not in PAYMENT_RATING_CODES:
            result.add_error("payment_rating", pr,
                             f"Invalid payment rating '{pr}'; must be one of: "
                             f"{', '.join(PAYMENT_RATING_CODES.keys())}",
                             "PR-002")
        elif status in ACCOUNT_STATUS_CODES and pr:
            allowed = STATUS_PAYMENT_RATING_MAP.get(status, list(PAYMENT_RATING_CODES.keys()))
            if pr not in allowed:
                result.add_error("payment_rating", pr,
                                 f"Payment rating '{pr}' is incompatible with "
                                 f"account status '{status}'. Allowed: {allowed}",
                                 "PR-003")

        # ── 12. Payment History Profile ──────────────────────────────────────
        php = str(r.get("payment_history_profile", "")).strip()
        if php:
            # Must be exactly 24 chars; pad if needed for dict-based input
            php_padded = php.ljust(24)[:24]
            invalid_chars = [c for c in php_padded if c not in PAYMENT_HISTORY_CODES]
            if invalid_chars:
                result.add_error("payment_history_profile", php,
                                 f"Payment history profile contains invalid characters: "
                                 f"{list(set(invalid_chars))}; "
                                 f"valid codes are: 0-6, B, D, E, G, H, J, K, U, space",
                                 "PHP-001")

        # ── 13. Special Comment ──────────────────────────────────────────────
        sc = str(r.get("special_comment", "  ")).strip()
        sc_padded = sc.ljust(2)[:2]
        if sc_padded not in SPECIAL_COMMENT_CODES and sc.strip():
            result.add_warning("special_comment", sc,
                               f"Unrecognized special comment code '{sc}'",
                               "SC-001")

        # ── 14. Compliance Condition Code ────────────────────────────────────
        ccc = str(r.get("compliance_condition_code", "  "))
        ccc_padded = ccc.ljust(2)[:2]
        if ccc_padded not in COMPLIANCE_CONDITION_CODES and ccc.strip():
            result.add_warning("compliance_condition_code", ccc,
                               f"Unrecognized compliance condition code '{ccc}'",
                               "CCC-001")

        # ── 15. Current Balance ──────────────────────────────────────────────
        cb_raw = str(r.get("current_balance", "")).strip()
        if cb_raw:
            if not re.fullmatch(r"\d+", cb_raw):
                result.add_error("current_balance", cb_raw,
                                 "Current balance must be numeric (right justified, zero filled)",
                                 "BAL-001")

        # ── 16. Amount Past Due ──────────────────────────────────────────────
        apd_raw = str(r.get("amount_past_due", "")).strip()
        if apd_raw:
            if not re.fullmatch(r"\d+", apd_raw):
                result.add_error("amount_past_due", apd_raw,
                                 "Amount past due must be numeric",
                                 "APD-001")
        # If account status indicates past-due, amount_past_due should be non-zero
        if status in {"71", "78", "80", "82", "83", "84"}:
            if not apd_raw or apd_raw == "0" or all(c == "0" for c in apd_raw):
                result.add_warning("amount_past_due", apd_raw,
                                   f"Account status '{status}' indicates past-due account "
                                   f"but amount past due is zero",
                                   "APD-002")

        # ── 17. Date of Account Information ─────────────────────────────────
        dai_raw = str(r.get("date_of_account_information", "")).strip()
        date_info = _parse_date(dai_raw)
        if not dai_raw or _is_zero_filled_date(dai_raw):
            result.add_error("date_of_account_information", dai_raw,
                             "Date of account information is required",
                             "DAI-001")
        elif date_info is None:
            result.add_error("date_of_account_information", dai_raw,
                             f"Invalid date format '{dai_raw}'; expected MMDDYYYY",
                             "DAI-002")
        elif date_info > today:
            result.add_error("date_of_account_information", dai_raw,
                             "Date of account information cannot be in the future",
                             "DAI-003")
        elif date_opened and date_info < date_opened:
            result.add_error("date_of_account_information", dai_raw,
                             "Date of account information cannot be before date opened",
                             "DAI-004")

        # ── 18. FCRA Compliance Date ─────────────────────────────────────────
        fcra_raw = str(r.get("fcra_compliance_date", "")).strip()
        fcra_date = _parse_date(fcra_raw)
        if status in DELINQUENCY_STATUS_CODES:
            if not fcra_raw or _is_zero_filled_date(fcra_raw):
                result.add_error("fcra_compliance_date", fcra_raw,
                                 f"FCRA compliance date is required when account status is "
                                 f"'{status}' (delinquent/charged-off/etc.)",
                                 "FCRA-001")
            elif fcra_date and date_opened and fcra_date < date_opened:
                result.add_error("fcra_compliance_date", fcra_raw,
                                 "FCRA compliance date cannot be before date opened",
                                 "FCRA-002")
            elif fcra_date and fcra_date > today:
                result.add_error("fcra_compliance_date", fcra_raw,
                                 "FCRA compliance date cannot be in the future",
                                 "FCRA-003")
        elif fcra_raw and not _is_zero_filled_date(fcra_raw) and fcra_date is None:
            result.add_error("fcra_compliance_date", fcra_raw,
                             f"Invalid date format '{fcra_raw}'; expected MMDDYYYY or 00000000",
                             "FCRA-004")

        # ── 19. Date Closed ──────────────────────────────────────────────────
        dc_raw = str(r.get("date_closed", "")).strip()
        date_closed = _parse_date(dc_raw)
        if dc_raw and not _is_zero_filled_date(dc_raw):
            if date_closed is None:
                result.add_error("date_closed", dc_raw,
                                 f"Invalid date format '{dc_raw}'; expected MMDDYYYY or 00000000",
                                 "DC-001")
            elif date_opened and date_closed < date_opened:
                result.add_error("date_closed", dc_raw,
                                 "Date closed cannot be before date opened",
                                 "DC-002")
            elif date_closed > today:
                result.add_error("date_closed", dc_raw,
                                 "Date closed cannot be in the future",
                                 "DC-003")

        # ── 20. Date of Last Payment ─────────────────────────────────────────
        dlp_raw = str(r.get("date_of_last_payment", "")).strip()
        date_last_pay = _parse_date(dlp_raw)
        if dlp_raw and not _is_zero_filled_date(dlp_raw):
            if date_last_pay is None:
                result.add_error("date_of_last_payment", dlp_raw,
                                 f"Invalid date format '{dlp_raw}'; expected MMDDYYYY or 00000000",
                                 "DLP-001")
            elif date_opened and date_last_pay < date_opened:
                result.add_error("date_of_last_payment", dlp_raw,
                                 "Date of last payment cannot be before date opened",
                                 "DLP-002")
            elif date_last_pay > today:
                result.add_error("date_of_last_payment", dlp_raw,
                                 "Date of last payment cannot be in the future",
                                 "DLP-003")

        # ── 21. Interest Type Indicator ──────────────────────────────────────
        iti = str(r.get("interest_type_indicator", "")).strip()
        if iti and iti not in INTEREST_TYPE_INDICATORS:
            result.add_warning("interest_type_indicator", iti,
                               f"Invalid interest type indicator '{iti}'; "
                               f"must be F, V, 0, or X",
                               "ITI-001")

        # ── 22. Social Security Number ───────────────────────────────────────
        ssn = str(r.get("social_security_number", "")).strip()
        if ssn:
            if not re.fullmatch(r"\d{9}", ssn):
                result.add_error("social_security_number", "***",
                                 "SSN must be exactly 9 digits (no dashes or spaces)",
                                 "SSN-001")
            elif ssn in ("000000000", "111111111", "123456789", "999999999"):
                result.add_error("social_security_number", "***",
                                 "SSN appears to be invalid (all same digits or sequential)",
                                 "SSN-002")

        # ── 23. Consumer Name ────────────────────────────────────────────────
        surname = str(r.get("consumer_name_surname", "")).strip()
        first = str(r.get("consumer_name_first", "")).strip()
        if not surname and not first:
            result.add_error("consumer_name_surname", "",
                             "Consumer surname or first name is required",
                             "NAME-001")
        if surname and len(surname) > 25:
            result.add_error("consumer_name_surname", surname,
                             f"Surname exceeds 25 characters (got {len(surname)})",
                             "NAME-002")
        if first and len(first) > 20:
            result.add_error("consumer_name_first", first,
                             f"First name exceeds 20 characters (got {len(first)})",
                             "NAME-003")

        # ── 24. Generation Code ──────────────────────────────────────────────
        gc = str(r.get("generation_code", " ")).strip()
        if gc and gc not in GENERATION_CODES:
            result.add_warning("generation_code", gc,
                               f"Invalid generation code '{gc}'; "
                               f"must be J, S, 2-9, or blank",
                               "GEN-001")

        # ── 25. Date of Birth ────────────────────────────────────────────────
        dob_raw = str(r.get("date_of_birth", "")).strip()
        if dob_raw and not _is_zero_filled_date(dob_raw):
            dob = _parse_date(dob_raw)
            if dob is None:
                result.add_error("date_of_birth", dob_raw,
                                 f"Invalid date of birth format '{dob_raw}'; expected MMDDYYYY",
                                 "DOB-001")
            elif dob > today:
                result.add_error("date_of_birth", dob_raw,
                                 "Date of birth cannot be in the future",
                                 "DOB-002")
            elif dob.year < 1900:
                result.add_warning("date_of_birth", dob_raw,
                                   "Date of birth year seems unusually old (before 1900)",
                                   "DOB-003")
            elif (today - dob).days < 365 * 10:
                result.add_warning("date_of_birth", dob_raw,
                                   "Consumer appears to be under 10 years old",
                                   "DOB-004")
            elif (today - dob).days > 365 * 125:
                result.add_warning("date_of_birth", dob_raw,
                                   "Consumer appears to be over 125 years old",
                                   "DOB-005")

        # ── 26. Telephone Number ─────────────────────────────────────────────
        tel = str(r.get("telephone_number", "")).strip()
        if tel and tel != "0000000000":
            if not re.fullmatch(r"\d{10}", tel):
                result.add_warning("telephone_number", tel,
                                   "Telephone must be 10 digits (no dashes); "
                                   f"got '{tel}'",
                                   "TEL-001")

        # ── 27. ECOA Code ────────────────────────────────────────────────────
        ecoa = str(r.get("ecoa_code", "")).strip()
        if not ecoa:
            result.add_error("ecoa_code", ecoa,
                             "ECOA code is required",
                             "ECOA-001")
        elif ecoa not in ECOA_CODES:
            result.add_error("ecoa_code", ecoa,
                             f"Invalid ECOA code '{ecoa}'; must be one of: "
                             f"{', '.join(ECOA_CODES.keys())}",
                             "ECOA-002")

        # ── 28. Consumer Information Indicator ───────────────────────────────
        cii = str(r.get("consumer_information_indicator", "  "))
        cii_padded = cii.ljust(2)[:2]
        if cii.strip() and cii_padded not in CONSUMER_INFO_INDICATORS:
            result.add_warning("consumer_information_indicator", cii,
                               f"Unrecognized consumer information indicator '{cii}'",
                               "CII-001")

        # ── 29. Address Fields ───────────────────────────────────────────────
        addr1 = str(r.get("first_line_of_address", "")).strip()
        city = str(r.get("city", "")).strip()
        state = str(r.get("state", "")).strip().upper()
        postal = str(r.get("postal_code", "")).strip()

        if state and state not in US_STATE_CODES and state != "":
            result.add_warning("state", state,
                               f"Unrecognized state code '{state}'",
                               "ADDR-001")

        if postal:
            if not re.fullmatch(r"[A-Z0-9]{5,9}", postal.replace("-", "")):
                result.add_warning("postal_code", postal,
                                   f"Postal code '{postal}' does not appear to be a valid "
                                   f"US ZIP or Canadian postal code",
                                   "ADDR-002")

        # ── 30. Address Indicator ────────────────────────────────────────────
        ai = str(r.get("address_indicator", "")).strip()
        if ai and ai not in ADDRESS_INDICATOR_CODES:
            result.add_warning("address_indicator", ai,
                               f"Invalid address indicator '{ai}'; "
                               f"must be one of: {', '.join(ADDRESS_INDICATOR_CODES.keys())}",
                               "ADDR-003")

        # ── 31. Residence Code ───────────────────────────────────────────────
        rc = str(r.get("residence_code", "")).strip()
        if rc and rc not in RESIDENCE_CODES:
            result.add_warning("residence_code", rc,
                               f"Invalid residence code '{rc}'; must be O, R, or blank",
                               "RC-001")

        # ── 32. Cross-field: Charge-off consistency ──────────────────────────
        co_raw = str(r.get("original_charge_off_amount", "")).strip()
        if status in {"93", "97"}:
            if not co_raw or all(c == "0" for c in co_raw):
                result.add_warning("original_charge_off_amount", co_raw,
                                   f"Account status '{status}' indicates charge-off "
                                   f"but original charge-off amount is zero",
                                   "CO-001")

        # ── 33. Cross-field: Closed account should have date closed ──────────
        if status in {"13", "62", "63", "64", "65", "05"} and \
                (not dc_raw or _is_zero_filled_date(dc_raw)):
            result.add_warning("date_closed", dc_raw,
                               f"Account status '{status}' indicates closed account "
                               f"but date closed is not populated",
                               "DC-004")

        # ── 34. Original Charge-off Amount ──────────────────────────────────
        if co_raw:
            if not re.fullmatch(r"\d+", co_raw):
                result.add_error("original_charge_off_amount", co_raw,
                                 "Original charge-off amount must be numeric",
                                 "CO-002")
