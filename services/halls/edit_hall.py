

def edit_hall(old_name,name,capacity,equipment,is_active,hall_repository):

    halls = hall_repository.get_all()

    selected_hall = None

    for hall in halls:
        if hall["name"].lower() == old_name.lower():
            selected_hall = hall
            break

    if selected_hall is None:
        raise ValueError("Hall not found.")

    name = name.strip()
    equipment = equipment.strip()

    if not name:
        raise ValueError("Hall name cannot be empty.")

    if not equipment:
        raise ValueError("Hall equipment cannot be empty.")

    try:
        capacity = int(capacity)
    except (ValueError, TypeError):
        raise ValueError("Hall capacity must be a number.")

    if capacity <= 0:
        raise ValueError("Hall capacity must be greater than zero.")

    for hall in halls:
        if (
            hall["name"].lower() == name.lower()
            and hall["name"].lower() != old_name.lower()
        ):
            raise ValueError("A hall with this name already exists.")

    updated = hall_repository.update(selected_hall["name"],name,capacity,equipment,is_active)

    if not updated:
        raise ValueError("Could not update hall.")

    return True
