import re


def validate_phone(phone):
    """Validate a 10-digit Indian phone number."""
    pattern = r"^[6-9]\d{9}$"

    return bool(re.fullmatch(pattern, phone))


def validate_email(email):
    """Validate an email address."""
    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"

    return bool(re.fullmatch(pattern, email))


def validate_name(name):
    """Validate that the contact name is not empty."""
    return bool(name.strip())