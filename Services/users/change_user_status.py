def change_user_status(username, role, is_active, user_repository):
    users = user_repository.get_all()

    selected_user = None

    for user in users:
        if user["username"] == username and user["role"] == role:
            selected_user = user
            break

    if selected_user is None:
        raise ValueError(f"{role.capitalize()} not found.")

    if selected_user["is_active"] == is_active:
        status = "active" if is_active else "inactive"
        raise ValueError(f"This {role} is already {status}.")

    updated = user_repository.update_status(username, role, is_active)

    if not updated:
        raise ValueError(f"Could not update {role} status.")

    return True
