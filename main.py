from contacts import (
    display_contacts,
    search_contacts,
    add_contact,
    update_contact,
    delete_contact
)

from exceptions import (
    ContactNotFoundError,
    DuplicateContactError
)


def show_menu():
    """Display the main menu."""

    print("\n")
    print("=" * 45)
    print("       CONTACT MANAGEMENT SYSTEM")
    print("=" * 45)
    print("1. Display Contacts")
    print("2. Search Contact")
    print("3. Add Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")
    print("=" * 45)


def search_contact_menu():
    """Handle contact search."""

    search_text = input(
        "\nEnter name, phone, or email to search: "
    )

    try:
        contacts = search_contacts(search_text)

        print("\nSearch Results")
        print("-" * 70)

        for contact in contacts:
            print(
                f"ID: {contact['id']} | "
                f"Name: {contact['name']} | "
                f"Phone: {contact['phone']} | "
                f"Email: {contact['email']}"
            )

    except ContactNotFoundError as error:
        print(f"\n{error}")


def add_contact_menu():
    """Handle adding a new contact."""

    try:
        name = input("\nEnter name: ")
        phone = input("Enter phone number: ")
        email = input("Enter email: ")

        add_contact(name, phone, email)

    except ValueError as error:
        print(f"\nError: {error}")

    except DuplicateContactError as error:
        print(f"\nError: {error}")


def update_contact_menu():
    """Handle updating a contact."""

    try:
        contact_id = int(
            input("\nEnter Contact ID: ")
        )

        name = input("Enter new name: ")
        phone = input("Enter new phone number: ")
        email = input("Enter new email: ")

        update_contact(
            contact_id,
            name,
            phone,
            email
        )

    except ValueError as error:
        print(f"\nError: {error}")

    except ContactNotFoundError as error:
        print(f"\nError: {error}")


def delete_contact_menu():
    """Handle deleting a contact."""

    try:
        contact_id = int(
            input("\nEnter Contact ID: ")
        )

        delete_contact(contact_id)

    except ValueError:
        print("\nPlease enter a valid Contact ID.")

    except ContactNotFoundError as error:
        print(f"\nError: {error}")


def main():
    """Run the Contact Management System."""

    while True:

        show_menu()

        choice = input("Enter your choice: ")

        if choice == "1":
            display_contacts()

        elif choice == "2":
            search_contact_menu()

        elif choice == "3":
            add_contact_menu()

        elif choice == "4":
            update_contact_menu()

        elif choice == "5":
            delete_contact_menu()

        elif choice == "6":
            print(
                "\nThank you for using "
                "Contact Management System."
            )
            break

        else:
            print("\nInvalid choice. Please try again.")


if __name__ == "__main__":
    main()