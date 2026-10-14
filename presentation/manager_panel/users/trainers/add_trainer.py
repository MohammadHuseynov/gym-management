from model.user import Trainer
from services.users.add_user import add_user
from services.validations.validation import (validate_email, validate_password, get_user_status)


def add_trainer(user_repository):
    name = input("Enter trainer name: ").strip()
    username = input("Enter username: ").strip()

    while True:
        password = input("Enter password: ")

        if validate_password(password):
            break

        else:
            print("Invalid password. Please try again.")

    while True:
        email = input("Enter email: ").strip()

        if validate_email(email):
            break

    print("Invalid email. Please try again.")

    is_active = get_user_status()

    trainer = Trainer(
        name,
        username,
        password,
        email,
        "trainer",
        is_active
    )

    try:
        add_user(trainer, user_repository)
        print("Trainer added successfully!")
        return True

    except ValueError as error:
        print(f"Error: {error}")
        return False