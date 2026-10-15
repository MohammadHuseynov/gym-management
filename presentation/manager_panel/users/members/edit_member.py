
from services.users.edit_user import edit_user
from services.validations.validation import (validate_email, validate_password, get_user_status)

def edit_member(user_repository):
    users = user_repository.get_all()

    members = [user for user in users if user["role"] == "member"]

    if not members:
        print("There are no members to edit.")
        return False

    old_username = input("Enter the username of the member to edit: ").strip()

    member = None

    for user in members:
        if user["username"] == old_username:
            member = user
            break

    if member is None:
        print("Member not found.")
        return False

    print("\nPress Enter to keep the current value.")

    
    current_name = member["name"]
    name_input = input(f"Name [{current_name}]: ").strip()
    name = name_input if name_input else current_name

    current_username = member["username"]

    while True:
        username_input = input(
            f"Username [{current_username}]: "
        ).strip()

        if not username_input:
            username = current_username
            break

        if username_input != old_username:
            if not user_repository.is_username_unique(username_input):
                print("Username already exists. Try another.")
                continue

        username = username_input
        break

    
    while True:
        password_input = input(
            "New password (press Enter to keep current): "
        )

        if not password_input:
            password = member["password"]
            break

        if validate_password(password_input):
            password = password_input
            break

        else:
            print("Invalid password. Please try again.")

    
    current_email = member["email"]

    while True:
        email_input = input(
            f"Email [{current_email}]: "
        ).strip()

        if not email_input:
            email = current_email
            break

        if validate_email(email_input):
            email = email_input
            break

        print("Invalid email. Please try again.")

    current_status = member["is_active"]
    status_text = "Active" if current_status else "Inactive"

    print(f"\nCurrent status: {status_text}")
    print("1. Keep current status")
    print("2. Change status")

    while True:
        status_choice = input("Choose (1-2): ").strip()

        if status_choice == "1":
            is_active = current_status
            break

        elif status_choice == "2":
            is_active = get_user_status()
            break

        else:
            print("Invalid choice. Please enter 1 or 2.")

    try:
        edit_user(
            old_username,
            name,
            username,
            password,
            email,
            "member",
            user_repository,
            is_active=is_active
        )

        print("Member updated successfully!")
        return True

    except ValueError as error:
        print(f"Error: {error}")
        return False
