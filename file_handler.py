import json


CONTACT_FILE = "data/contacts.json"


def load_contacts():
    """Load contacts from the JSON file."""

    try:
        with open(CONTACT_FILE, "r") as file:
            return json.load(file)

    except FileNotFoundError:
        return []

    except json.JSONDecodeError:
        return []


def save_contacts(contacts):
    """Save contacts to the JSON file."""

    with open(CONTACT_FILE, "w") as file:
        json.dump(contacts, file, indent=4)