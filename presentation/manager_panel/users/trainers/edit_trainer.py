
from services.users.edit_user import edit_user
from services.validations.validation import (validate_email,validate_password,get_user_status)


def edit_trainer(user_repository):
    old_username = input("Enter the username of the trainer to edit (or 1 to go back): ").strip()

    if old_username.lower() == "1":
        return False

    users = user_repository.get_all()

    trainer_found = False

    for user in users:
        if (user["username"] == old_username and user["role"] == "trainer"):
            trainer_found = True
            break

    if not trainer_found:
        print("Trainer not found.")
        return False

    name = input("Enter new name: ").strip()

    while True:
        username = input("Enter new username: ").strip()

        if not username:
            print("Username cannot be empty.")
            continue

        if username != old_username:
            if not user_repository.is_username_unique(username):
                print("Username already exists. Try another.")
                continue

        break

    while True:
        password = input("Enter new password: ")

        if validate_password(password):
            break

        print("Invalid password. Please try again.")

    while True:
        email = input("Enter new email: ").strip()

        if validate_email(email):
            break

        print("Invalid email. Please try again.")

    print("Select the trainer status: ")
    is_active = get_user_status()

    try:
        edit_user(
            old_username,
            name,
            username,
            password,
            email,
            "trainer",
            user_repository,
            is_active=is_active
        )

        print("Trainer updated successfully!")
        return True

    except ValueError as error:
        print(f"Error: {error}")
        return False
