from services.validations.validation import (validate_email,validate_password)

def edit_user(
    old_username,
    name,
    username,
    password,
    email,
    role,
    user_repository,
    is_active=None
):
    users = user_repository.get_all()

    selected_user = None

    for user in users:
        if user["username"] == old_username:
            selected_user = user
            break

    if selected_user is None:
        raise ValueError("User not found.")

    if selected_user["role"] != role:
        raise ValueError(f"The selected user is not a {role}.")

    name = name.strip()
    username = username.strip()
    email = email.strip()

    if not name:
        raise ValueError("Name cannot be empty.")

    if not username:
        raise ValueError("Username cannot be empty.")

    if username != old_username:
        if not user_repository.is_username_unique(username):
            raise ValueError("Username already exists.")

    if not validate_password(password):
        raise ValueError("Invalid password.")

    if not validate_email(email):
        raise ValueError("Invalid email.")

    updated = user_repository.update(
        old_username,
        name,
        username,
        password,
        email,
        is_active
    )

    if not updated:
        raise ValueError("User not found.")

    return True
