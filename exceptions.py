class ContactNotFoundError(Exception):
    """Raised when a contact cannot be found."""
    pass


class DuplicateContactError(Exception):
    """Raised when a duplicate contact is detected."""
    pass