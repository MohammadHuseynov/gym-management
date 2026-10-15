from services.validations.validation import validate_password, validate_email


def add_user(user, user_repository):
    if not user.name.strip():
        raise ValueError("Name cannot be empty.")

    if not user.username.strip():
        raise ValueError("Username cannot be empty.")

    if not user_repository.is_username_unique(user.username):
        raise ValueError("Username already exists.")

    if not validate_password(user.password):
        raise ValueError(
            "Password must contain an English letter, "
            "a number, and either @ or &."
        )

    if not validate_email(user.email):
        raise ValueError("Email is not valid.")

    if user.role not in ("trainer", "member"):
        raise ValueError("Role must be trainer or member.")

    user_repository.add(user)
