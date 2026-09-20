from file_handler import load_contacts, save_contacts
from exceptions import ContactNotFoundError, DuplicateContactError
from validators import validate_phone, validate_email, validate_name


def display_contacts():
    """Display all contacts."""

    contacts = load_contacts()

    if not contacts:
        print("\nNo contacts available.")
        return

    print("\nContact List")
    print("-" * 75)
    print(
        f"{'ID':<5}"
        f"{'Name':<25}"
        f"{'Phone':<15}"
        f"{'Email':<30}"
    )
    print("-" * 75)

    for contact in contacts:
        print(
            f"{contact['id']:<5}"
            f"{contact['name']:<25}"
            f"{contact['phone']:<15}"
            f"{contact['email']:<30}"
        )


def search_contacts(search_text):
    """Search contacts by name, phone, or email."""

    contacts = load_contacts()

    search_text = search_text.lower()

    matching_contacts = [
        contact
        for contact in contacts
        if (
            search_text in contact["name"].lower()
            or search_text in contact["phone"]
            or search_text in contact["email"].lower()
        )
    ]

    if not matching_contacts:
        raise ContactNotFoundError("No matching contact found.")

    return matching_contacts


def add_contact(name, phone, email):
    """Add a new contact."""

    if not validate_name(name):
        raise ValueError("Name cannot be empty.")

    if not validate_phone(phone):
        raise ValueError(
            "Phone number must contain 10 digits "
            "and start with 6-9."
        )

    if not validate_email(email):
        raise ValueError("Invalid email address.")

    contacts = load_contacts()

    for contact in contacts:
        if contact["phone"] == phone:
            raise DuplicateContactError(
                "A contact with this phone number already exists."
            )

        if contact["email"].lower() == email.lower():
            raise DuplicateContactError(
                "A contact with this email already exists."
            )

    new_id = max(
        [contact["id"] for contact in contacts],
        default=0
    ) + 1

    new_contact = {
        "id": new_id,
        "name": name,
        "phone": phone,
        "email": email
    }

    contacts.append(new_contact)

    save_contacts(contacts)

    print("\nContact added successfully.")


def update_contact(contact_id, name, phone, email):
    """Update an existing contact."""

    if not validate_name(name):
        raise ValueError("Name cannot be empty.")

    if not validate_phone(phone):
        raise ValueError("Invalid phone number.")

    if not validate_email(email):
        raise ValueError("Invalid email address.")

    contacts = load_contacts()

    for contact in contacts:

        if contact["id"] == contact_id:

            contact["name"] = name
            contact["phone"] = phone
            contact["email"] = email

            save_contacts(contacts)

            print("\nContact updated successfully.")
            return

    raise ContactNotFoundError("Contact not found.")


def delete_contact(contact_id):
    """Delete a contact using its ID."""

    contacts = load_contacts()

    for contact in contacts:

        if contact["id"] == contact_id:

            contacts.remove(contact)

            save_contacts(contacts)

            print("\nContact deleted successfully.")
            return

    raise ContactNotFoundError("Contact not found.")


def get_contact(contact_id):
    """Get a contact using its ID."""

    contacts = load_contacts()

    for contact in contacts:
        if contact["id"] == contact_id:
            return contact

    raise ContactNotFoundError("Contact not found.")