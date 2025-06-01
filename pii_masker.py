import re

# Define regular expressions for each PII type
PII_PATTERNS = {
    "phone_number": r"(?:(?:\+?\d{1,3})?[-.\s]?)?(?:\d{1,4}[-.\s]?){2,5}\d{2,4}",
    "dob": r"\b\d{1,2}[/\-]\d{1,2}[/\-]\d{2,4}\b",
    "cvv_no": r"(?<!\d)\b\d{3}\b(?!\d)",
    "aadhar_num": r"\b\d{4} \d{4} \d{4}\b",
    "credit_debit_no": r"\b(?:\d[ -]*?){13,16}\b",
    "expiry_no": r"\b(0[1-9]|1[0-2])[/\-]([0-9]{2}|[0-9]{4})\b",
    "email": r"\b[\w\.-]+@[\w\.-]+\.\w+\b",
    "full_name": r"\b[A-Z][a-z]+ [A-Z][a-z]+\b"
}

# Mask all detected PII in the input text
def mask_pii(text):
    pattern_order = list(PII_PATTERNS.keys())
    matches = []

    for label in pattern_order:
        pattern = re.compile(PII_PATTERNS[label])
        for match in pattern.finditer(text):
            start, end = match.span()
            if any(s < end and start < e for s, e, _, _ in matches):
                continue  # Avoid overlapping PII matches
            matches.append((start, end, label, match.group()))

    matches.sort(key=lambda x: x[0])
    masked_text = []
    last_idx = 0

    for start, end, label, entity in matches:
        masked_text.append(text[last_idx:start])
        masked_text.append(f"[{label}]")
        last_idx = end

    masked_text.append(text[last_idx:])

    return "".join(masked_text), [
        {
            "position": [start, end],
            "classification": label,
            "entity": entity
        } for (start, end, label, entity) in matches
    ]
