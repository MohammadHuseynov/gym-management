def change_hall_status(name, is_active, hall_repository):
    halls = hall_repository.get_all()
    selected_hall = None

    for hall in halls:
        if hall["name"].lower() == name.lower():
            selected_hall = hall
            break

    if selected_hall is None:
        raise ValueError("Hall not found.")

    if selected_hall["is_active"] == is_active:
        status = "active" if is_active else "inactive"
        raise ValueError(f"This hall is already {status}.")

    updated = hall_repository.update_status(
        selected_hall["name"],
        is_active
    )

    if not updated:
        raise ValueError("Could not update hall status.")

    return True
