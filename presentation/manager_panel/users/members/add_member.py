from model.user import Member
from services.users.add_user import add_user
from services.validations.validation import (validate_email, validate_password,get_user_status)


def add_member(user_repository):
    name = input("Enter member name: ").strip()
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

    member = Member(
        name,
        username,
        password,
        email,
        "member",
        0,
        None,
        is_active
    )

    try:
        add_user(member, user_repository)
        print("Member added successfully!")
        return True

    except ValueError as error:
        print(f"Error: {error}")
        return False
