"""Metro 2 Format Constants — CDIA Metro 2 Format Reference Guide."""

# ── Portfolio Types ────────────────────────────────────────────────────────────
PORTFOLIO_TYPES = {
    "C": "Credit Card",
    "I": "Installment Loan",
    "M": "Mortgage",
    "O": "Open Account",
    "R": "Revolving Account",
}

# ── Account Type Codes ─────────────────────────────────────────────────────────
ACCOUNT_TYPES = {
    "00": "Auto",
    "01": "Unsecured",
    "02": "Secured",
    "03": "Partial Secured",
    "04": "Home Improvement",
    "05": "Student Loan",
    "06": "Business Credit Card",
    "07": "Conventional Real Estate Mortgage",
    "08": "Home Equity",
    "09": "Medical Debt",
    "10": "Home Equity Line of Credit (HELOC)",
    "11": "Manufactured Housing",
    "12": "Education",
    "13": "Note Loan",
    "14": "Secured by Household Goods",
    "15": "Combined Credit Plan",
    "16": "FHA Real Estate Mortgage",
    "17": "VA Real Estate Mortgage",
    "18": "Conv. Real Estate Mortgage, junior lien",
    "19": "Manufactured Housing, junior lien",
    "20": "Secured Credit Card",
    "21": "Retail Account",
    "22": "Utility Company Account",
    "23": "Telecom Company",
    "24": "Child/Spousal Support",
    "25": "Attorney Fees",
    "26": "Attorney Fees (Legal))",
    "27": "Agricultural Loan",
    "28": "Construction Loan",
    "29": "Religious Organization",
    "30": "Vacation/Timeshare",
    "31": "Recreational Merchandise",
    "32": "FHA Home Improvement",
    "33": "Government Unsecured Guaranteed",
    "34": "Government Secured Guaranteed",
    "35": "Government Home Improvement",
    "36": "Government Overpayment (non-student loans)",
    "37": "Government Fine",
    "38": "Government Employee Advance",
    "39": "Government Miscellaneous Debt",
    "40": "Time Share Loan",
    "41": "Secondary Education",
    "42": "Credit Line Secured",
    "43": "Debt Consolidation",
    "44": "Deposit Related",
    "45": "Premium Financing",
    "46": "Used Auto Leased",
    "47": "New Auto Leased",
    "48": "Business/Commercial",
    "49": "Taxes (Government)",
    "50": "Unknown",
    "51": "Collection Department / Agency / Attorney",
    "52": "Factoring Company Account",
    "53": "Home Improvement Loan - Junior Lien",
    "54": "FHA Home Improvement - Junior Lien",
    "55": "Business Line - Personally Guaranteed",
    "56": "Bicycle Loan",
    "57": "Boat Loan",
    "58": "Motorcycle Loan",
    "59": "Personal Line of Credit",
    "60": "Payday Loan",
    "61": "Returned Check",
    "62": "Installment Sales Contract",
    "63": "Fleet Lease",
    "64": "Fleet Non-Lease",
    "65": "Rental Agreement",
    "66": "Summary of Accounts (condense)",
    "67": "Line of Credit - Secured",
    "68": "Line of Credit - Unsecured",
    "69": "FHA Home Equity Conversion Mortgage (HECM) - Reverse Mortgage",
    "70": "Balance Transfer",
    "71": "Rent-to-Own",
    "72": "Manufactured Housing - Senior Lien",
    "73": "Commercial Installment Loan",
    "74": "Commercial Line of Credit",
    "75": "Commercial Mortgage",
    "76": "Charge Account",
    "77": "Non-Residential Real Estate",
    "78": "Home Equity Loan - Senior Lien",
    "79": "Home Equity Loan - Junior Lien",
    "80": "Lease",
    "81": "VA Home Improvement",
    "82": "Commercial Lease",
    "83": "Salary/Wages",
    "84": "Overdraft Protection",
    "85": "Flexible Spending Credit Card",
    "86": "Secured Line of Credit",
    "87": "Secured Installment Loan",
    "88": "Equity Based Line of Credit - Second Lien",
    "89": "Equity Based Line of Credit - Third or Higher Lien",
    "90": "Auto Dealer Draft (Floor Plan)",
    "91": "Solar Energy Loan",
    "92": "Other",
    "93": "Other — Educational",
    "94": "Collection",
    "95": "Sale Proceeds",
    "96": "Secured Business Credit Card",
    "97": "Charge-off",
    "98": "Debt Buyer",
    "99": "Authorized User",
}

# ── Account Status Codes ───────────────────────────────────────────────────────
ACCOUNT_STATUS_CODES = {
    "05": "Account transferred",
    "11": "Current account (paid as agreed)",
    "13": "Paid or closed account/zero balance",
    "61": "Account paid in full; was a collection account",
    "62": "Paid in full; no balance owing on this account",
    "63": "Account paid in full for less than full balance",
    "64": "Account legally paid in full for less than full amount",
    "65": "Paid in full; creditor is collection division of credit grantor",
    "71": "Account 30-59 days past due date",
    "78": "Account 60-89 days past due date",
    "80": "Account 90-119 days past due date",
    "82": "Account 120-149 days past due date",
    "83": "Account 150-179 days past due date",
    "84": "Account 180 or more days past due date",
    "86": "Transferred to third party",
    "87": "First payment never received",
    "88": "Claim filed with government for insurance",
    "89": "Deed received (in lieu of foreclosure on a defaulted mortgage; to satisfy the debt)",
    "90": "Chapter 7 (straight bankruptcy; debt discharged)",
    "91": "Chapter 11 (business reorganization)",
    "92": "Chapter 12 (adjustment of debts; family farmer)",
    "93": "Unpaid balance reported as a loss by credit grantor",
    "94": "Repossession (and possibly a deficiency balance exists)",
    "95": "Voluntary surrender; and possibly a deficiency balance",
    "96": "Merchandise was repossessed by credit grantor; there may be a deficiency balance",
    "97": "Unpaid balance; reported as a loss; less than full balance",
    "DA": "Delete Account",
}

# ── Payment Rating Codes ───────────────────────────────────────────────────────
PAYMENT_RATING_CODES = {
    "0": "Current; paid or paying as agreed",
    "1": "30-59 days past due",
    "2": "60-89 days past due",
    "3": "90-119 days past due",
    "4": "120-149 days past due",
    "5": "150-179 days past due",
    "6": "180 or more days past due",
    "B": "No payment history available prior to this time",
    "D": "No payment history available for this reporting period",
    "E": "Zero balance and current account",
    "G": "Collection; charge-off",
}

# ── Payment History Profile Codes ─────────────────────────────────────────────
PAYMENT_HISTORY_CODES = set("0123456BDEGHJKU ")

# ── Terms Frequency Codes ──────────────────────────────────────────────────────
TERMS_FREQUENCY_CODES = {
    "D": "Deferred",
    "W": "Weekly",
    "B": "Biweekly",
    "S": "Semimonthly (twice a month)",
    "M": "Monthly",
    "L": "Bimonthly (every two months)",
    "P": "Quarterly",
    "T": "Tri-annual (three times yearly)",
    "Y": "Annual",
    "1": "Single Payment Loan",
    "2": "Payment Frequency Unknown",
    "3": "Irregular",
    "X": "Not Reported / N/A",
}

# ── ECOA Codes ─────────────────────────────────────────────────────────────────
ECOA_CODES = {
    "1": "Individual account",
    "2": "Joint contractual liability",
    "3": "Undesignated",
    "4": "Joint user",
    "5": "Co-maker or guarantor",
    "6": "On behalf of another person (maker, primary borrower, etc.)",
    "7": "Maker",
    "8": "Deceased (subscriber, account holder)",
    "9": "Sign or guarantee only",
    "B": "Individual account for business",
    "T": "Terminated",
    "W": "Business / Commercial",
    "X": "Deceased (co-borrower / joint account holder)",
    "Z": "Delete consumer",
}

# ── Special Comment Codes ──────────────────────────────────────────────────────
SPECIAL_COMMENT_CODES = {
    "  ": "N/A",
    "AC": "Payroll deduction",
    "AH": "Purchased by another company",
    "AI": "Recalled to active military duty",
    "AM": "Account payments assured by wage earner plan or similar arrangement",
    "AN": "Account acquired by FDIC or NCUA",
    "AO": "Account sold to another lender",
    "AP": "Credit Line Suspended",
    "AS": "Account closed due to inactivity",
    "AT": "Account closed at credit grantor's request",
    "AU": "Account paid in full for less than the full balance",
    "AV": "First payment never received",
    "AW": "Affected by natural or declared disaster",
    "AX": "Forbearance",
    "AZ": "On-going account dispute by consumer",
    "BA": "Transferred to another office",
    "BB": "Account information disputed by consumer",
    "BC": "Active duty military",
    "BD": "No payments required",
    "BK": "Charge-off amount",
    "BL": "Credit card lost or stolen",
    "BN": "Paid by company which originally sold the merchandise",
    "BO": "Foreclosure proceedings started",
    "BP": "Paid through insurance",
    "BQ": "Redeemed or reinstated repossession",
    "BS": "Account closed due to government order",
    "BT": "Credit line reduced due to collateral depreciation",
    "BU": "Credit line reduced to comply with regulatory requirements",
    "BV": "Immediate repayment required per account agreement",
    "BW": "Identity theft (account closed and fraudulent information deleted)",
    "BX": "Identity theft (fraudulent information deleted from account)",
    "BY": "Internet / phone activity",
    "BZ": "Paid from proceeds of collateral",
    "CA": "Asset marked for repossession",
    "CB": "Payoff amount (balloon payment)",
    "CC": "Discharged through bankruptcy chapter 7",
    "CH": "Purchased by another company through securitization",
    "CI": "Account paid for less than full balance per settlement agreement",
    "CJ": "Account paid for less than full balance - payment deferred to future date",
    "CK": "Account closed and transferred to bankruptcy",
    "CL": "Account closed; Consumer objection to credit terms",
    "CM": "Account discharged through Chapter 7 bankruptcy",
    "CN": "Account included in Chapter 7 bankruptcy",
}

# ── Compliance Condition Codes ─────────────────────────────────────────────────
COMPLIANCE_CONDITION_CODES = {
    "  ": "N/A",
    "XA": "Account closed at consumer's request",
    "XB": "Account information disputed by consumer (FCRA Relevant)",
    "XC": "Completed investigation of FCRA dispute; consumer disagrees",
    "XD": "Account closed at consumer's request; consumer disputes information",
    "XE": "Dispute resolved; consumer disagrees",
    "XF": "Account subject to an IAPB agreement",
    "XG": "Employee dispute",
    "XH": "Dispute resolution - consumer disagrees",
    "XJ": "Account closed and transferred",
    "XK": "Active duty military",
    "XL": "Active duty military - account closed at consumer's request",
    "XM": "Active duty military - account disputed",
    "XN": "Account information disputed by consumer (FCRA Relevant) - complete and accurate",
    "XO": "Dispute resolved; customer disagrees; account closed per customer request",
    "XP": "Account transferred; account closed per customer request",
    "XR": "Dispute resolved; customer disagrees; account closed",
    "XS": "Dispute resolved",
    "XT": "Dispute resolved per the Fair Debt Collection Practices Act",
    "XW": "Dispute under investigation",
}

# ── Consumer Information Indicators ───────────────────────────────────────────
CONSUMER_INFO_INDICATORS = {
    "  ": "N/A",
    "A ": "Petition for Chapter 7 bankruptcy",
    "B ": "Petition for Chapter 11 bankruptcy",
    "C ": "Petition for Chapter 12 bankruptcy",
    "D ": "Petition for Chapter 13 bankruptcy",
    "E ": "Discharged through bankruptcy Chapter 7",
    "F ": "Discharged through bankruptcy Chapter 11",
    "G ": "Discharged/dismissed through bankruptcy Chapter 12",
    "H ": "Discharged through bankruptcy Chapter 13",
    "I ": "Chapter 7 bankruptcy dismissed",
    "J ": "Chapter 11 bankruptcy dismissed",
    "K ": "Chapter 12 bankruptcy dismissed",
    "L ": "Chapter 13 bankruptcy dismissed",
    "M ": "Reaffirmation of debt",
    "N ": "Reaffirmation of debt rescinded; Chapter 7 bankruptcy",
    "O ": "Relief from stay",
    "P ": "Non-petitioning spouse; Chapter 7",
    "Q ": "Non-petitioning spouse; Chapter 11",
    "R ": "Non-petitioning spouse; Chapter 12",
    "S ": "Non-petitioning spouse; Chapter 13",
    "T ": "Credit grantor cannot locate consumer",
    "U ": "Consumer now located; previous status was T",
    "V ": "Reaffirmation of debt rescinded",
    "W ": "Credit grantor does not have to report",
}

# ── Interest Type Indicator ────────────────────────────────────────────────────
INTEREST_TYPE_INDICATORS = {
    "F": "Fixed rate",
    "V": "Variable rate",
    "0": "Not applicable (credit card, line of credit)",
    "X": "Unknown",
}

# ── Generation Codes ───────────────────────────────────────────────────────────
GENERATION_CODES = set("JS23456789 ")

# ── Address Indicator Codes ────────────────────────────────────────────────────
ADDRESS_INDICATOR_CODES = {
    "C": "Confirmed/verified address (current address)",
    "N": "Not confirmed address (current address)",
    "Y": "Known to be address of consumer (current address)",
    "B": "Bill to address of consumer (not current address)",
    "U": "Non-deliverable address; returned mail",
    "D": "Data reporter's default address",
    "P": "Address of consumer's employer",
}

# ── Residence Code ─────────────────────────────────────────────────────────────
RESIDENCE_CODES = {
    "O": "Owns",
    "R": "Rents",
    " ": "N/A",
}

# ── US State Codes ─────────────────────────────────────────────────────────────
US_STATE_CODES = {
    "AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DE", "FL", "GA",
    "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD",
    "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ",
    "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC",
    "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY",
    "DC", "AS", "GU", "MP", "PR", "VI",  # territories
    "AB", "BC", "MB", "NB", "NL", "NS", "NT", "NU", "ON", "PE",  # Canadian
    "QC", "SK", "YT",
    "  ",  # blank / not applicable
}

# ── Record Types ───────────────────────────────────────────────────────────────
RECORD_DESCRIPTOR_WORD = "0426"

PROCESSING_INDICATORS = {
    "1": "Normal reporting",
    "2": "DA (Delete Account)",
    " ": "N/A (Header/Trailer)",
}

# ── Status-to-Payment Rating Compatibility Matrix ─────────────────────────────
# Maps account status to allowed payment ratings
STATUS_PAYMENT_RATING_MAP = {
    "05": list("0BDEG"),
    "11": ["0", "E"],
    "13": ["0", "E"],
    "61": list("0BDEG"),
    "62": list("0BDEG"),
    "63": list("0BDEG"),
    "64": list("0BDEG"),
    "65": list("0BDEG"),
    "71": ["1"],
    "78": ["2"],
    "80": ["3"],
    "82": ["4"],
    "83": ["5"],
    "84": ["6"],
    "86": list("0BDEG"),
    "87": list("0123456BDEG"),
    "88": list("0BDEG"),
    "89": list("0BDEG"),
    "90": list("0BDEG"),
    "91": list("0BDEG"),
    "92": list("0BDEG"),
    "93": ["G"],
    "94": list("0BDEG"),
    "95": list("0BDEG"),
    "96": list("0BDEG"),
    "97": ["G"],
    "DA": list("0BDEG"),
}

# ── Delinquency Status Codes (require FCRA Compliance Date) ───────────────────
DELINQUENCY_STATUS_CODES = {
    "71", "78", "80", "82", "83", "84",
    "93", "94", "95", "96", "97",
    "90", "91", "92",
}
