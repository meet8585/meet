"""Metro 2 Field definitions — position, length, type, and validation rules."""

from dataclasses import dataclass, field
from typing import Optional, Callable, Any


@dataclass
class FieldDefinition:
    """Defines a single Metro 2 field."""

    name: str
    start: int        # 1-based position in the fixed-width record
    length: int
    field_type: str   # 'N'=Numeric, 'AN'=Alphanumeric, 'A'=Alpha
    required: bool = True
    description: str = ""
    validators: list[Callable] = field(default_factory=list)

    @property
    def end(self) -> int:
        return self.start + self.length - 1

    def extract(self, record: str) -> str:
        """Extract this field's raw value from a fixed-width record."""
        if len(record) < self.end:
            return ""
        return record[self.start - 1 : self.end]


# ── Header Record Fields (426 chars) ──────────────────────────────────────────
HEADER_FIELDS: list[FieldDefinition] = [
    FieldDefinition("record_descriptor_word", 1, 4, "N",
                    description="Must be '0426'"),
    FieldDefinition("processing_indicator", 5, 1, "AN",
                    description="Processing indicator"),
    FieldDefinition("cycle_number", 6, 6, "N",
                    description="Cycle date MMDDYY"),
    FieldDefinition("reporter_name", 12, 40, "AN",
                    description="Name of the reporting entity"),
    FieldDefinition("reporter_address", 52, 96, "AN",
                    description="Address of reporting entity"),
    FieldDefinition("reporter_telephone", 148, 10, "N",
                    description="10-digit phone number"),
    FieldDefinition("software_vendor_name", 158, 40, "AN", required=False,
                    description="Software vendor name"),
    FieldDefinition("software_version_number", 198, 20, "AN", required=False,
                    description="Software version"),
    FieldDefinition("prbc_program_identifier", 218, 10, "AN", required=False,
                    description="PRBC program identifier"),
    FieldDefinition("reserved", 228, 199, "AN", required=False,
                    description="Reserved — blank fill"),
]

# ── Base Segment Fields (426 chars) ───────────────────────────────────────────
BASE_SEGMENT_FIELDS: list[FieldDefinition] = [
    FieldDefinition("record_descriptor_word", 1, 4, "N",
                    description="Must be '0426'"),
    FieldDefinition("processing_indicator", 5, 1, "AN",
                    description="1=Normal, 2=DA (Delete Account)"),
    FieldDefinition("account_number", 6, 20, "AN",
                    description="Subscriber account number (left justified, blank filled)"),
    FieldDefinition("portfolio_type", 26, 1, "A",
                    description="C=Credit Card, I=Installment, M=Mortgage, O=Open, R=Revolving"),
    FieldDefinition("account_type", 27, 2, "AN",
                    description="Account type code (00-99)"),
    FieldDefinition("date_opened", 29, 8, "N",
                    description="Date account opened MMDDYYYY"),
    FieldDefinition("credit_limit", 37, 9, "N", required=False,
                    description="Credit limit or highest credit amount (right justified, zero filled)"),
    FieldDefinition("terms_duration", 46, 3, "AN", required=False,
                    description="Number of months or term code (LOC, REV, MIN, 001-999)"),
    FieldDefinition("terms_frequency", 49, 1, "AN",
                    description="Payment frequency code"),
    FieldDefinition("scheduled_monthly_payment_amount", 50, 9, "N", required=False,
                    description="Scheduled payment amount"),
    FieldDefinition("actual_payment_amount", 59, 9, "N", required=False,
                    description="Actual payment amount received"),
    FieldDefinition("account_status", 68, 2, "AN",
                    description="Account status code"),
    FieldDefinition("payment_rating", 70, 1, "AN",
                    description="Payment rating code"),
    FieldDefinition("payment_history_profile", 71, 24, "AN",
                    description="24-month payment history (most recent first)"),
    FieldDefinition("special_comment", 95, 2, "AN", required=False,
                    description="Special comment code"),
    FieldDefinition("compliance_condition_code", 97, 2, "AN", required=False,
                    description="FCRA compliance condition code"),
    FieldDefinition("current_balance", 99, 9, "N",
                    description="Current outstanding balance"),
    FieldDefinition("amount_past_due", 108, 9, "N", required=False,
                    description="Amount past due"),
    FieldDefinition("original_charge_off_amount", 117, 9, "N", required=False,
                    description="Original charge-off amount"),
    FieldDefinition("date_of_account_information", 126, 8, "N",
                    description="As-of date for account info MMDDYYYY"),
    FieldDefinition("fcra_compliance_date", 134, 8, "N", required=False,
                    description="FCRA compliance / first delinquency date MMDDYYYY"),
    FieldDefinition("date_closed", 142, 8, "N", required=False,
                    description="Date account closed MMDDYYYY (00000000 if N/A)"),
    FieldDefinition("date_of_last_payment", 150, 8, "N", required=False,
                    description="Date of most recent payment MMDDYYYY"),
    FieldDefinition("interest_type_indicator", 158, 1, "AN", required=False,
                    description="F=Fixed, V=Variable, 0=N/A, X=Unknown"),
    FieldDefinition("reserved_1", 159, 1, "AN", required=False,
                    description="Reserved — blank"),
    FieldDefinition("social_security_number", 160, 9, "N", required=False,
                    description="Consumer SSN (9 digits, no dashes)"),
    FieldDefinition("consumer_name_surname", 169, 25, "AN",
                    description="Last name (left justified, blank filled)"),
    FieldDefinition("consumer_name_first", 194, 20, "AN",
                    description="First name (left justified, blank filled)"),
    FieldDefinition("consumer_name_middle", 214, 20, "AN", required=False,
                    description="Middle name/initial (left justified, blank filled)"),
    FieldDefinition("generation_code", 234, 1, "AN", required=False,
                    description="J=Jr, S=Sr, 2-9=II-IX, blank=N/A"),
    FieldDefinition("date_of_birth", 235, 8, "N", required=False,
                    description="Date of birth MMDDYYYY"),
    FieldDefinition("telephone_number", 243, 10, "N", required=False,
                    description="10-digit telephone (no dashes)"),
    FieldDefinition("ecoa_code", 253, 1, "AN",
                    description="Equal Credit Opportunity Act code"),
    FieldDefinition("consumer_information_indicator", 254, 2, "AN", required=False,
                    description="Bankruptcy / special indicator"),
    FieldDefinition("country_code", 256, 2, "AN", required=False,
                    description="Two-letter country code (US, blank=USA)"),
    FieldDefinition("first_line_of_address", 258, 32, "AN", required=False,
                    description="Street address line 1"),
    FieldDefinition("second_line_of_address", 290, 32, "AN", required=False,
                    description="Street address line 2"),
    FieldDefinition("city", 322, 20, "AN", required=False,
                    description="City name"),
    FieldDefinition("state", 342, 2, "AN", required=False,
                    description="Two-letter state code"),
    FieldDefinition("postal_code", 344, 9, "AN", required=False,
                    description="ZIP or postal code (no dash)"),
    FieldDefinition("address_indicator", 353, 1, "AN", required=False,
                    description="C=Confirmed, N=Not confirmed, Y=Known, B=Bill-to, U=Undeliverable"),
    FieldDefinition("residence_code", 354, 1, "AN", required=False,
                    description="O=Owns, R=Rents, blank=N/A"),
    FieldDefinition("segments", 355, 72, "AN", required=False,
                    description="J1/J2/K1-K4/L1/N1 optional sub-segments"),
]

# ── Trailer Record Fields ──────────────────────────────────────────────────────
TRAILER_FIELDS: list[FieldDefinition] = [
    FieldDefinition("record_descriptor_word", 1, 4, "N",
                    description="Must be '0426'"),
    FieldDefinition("processing_indicator", 5, 1, "AN",
                    description="Processing indicator"),
    FieldDefinition("total_base_records", 6, 9, "N",
                    description="Total number of base segment records"),
    FieldDefinition("reserved_1", 15, 9, "AN", required=False),
    FieldDefinition("total_status_code_df", 24, 9, "N", required=False,
                    description="Total accounts with DA status"),
    FieldDefinition("reserved_2", 33, 9, "AN", required=False),
    FieldDefinition("total_consumer_segments_j1", 42, 9, "N", required=False,
                    description="Total J1 sub-segments"),
    FieldDefinition("total_consumer_segments_j2", 51, 9, "N", required=False,
                    description="Total J2 sub-segments"),
    FieldDefinition("block_count", 60, 9, "N",
                    description="Total records including header and trailer"),
    FieldDefinition("reserved_3", 69, 358, "AN", required=False),
]
