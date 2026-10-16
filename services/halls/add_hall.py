
from model.hall import Hall


def add_hall(name, capacity, equipment, hall_repository):
    name = name.strip()
    equipment = equipment.strip()

    if not name:
        raise ValueError("Hall name cannot be empty.")

    if not capacity:
        raise ValueError("Hall capacity cannot be empty.")

    try:
        capacity = int(capacity)
    except ValueError:
        raise ValueError("Hall capacity must be a number.")

    if capacity <= 0:
        raise ValueError("Hall capacity must be greater than zero.")

    if not equipment:
        raise ValueError("Hall equipment cannot be empty.")

    halls = hall_repository.get_all()

    for hall in halls:
        if hall["name"].lower() == name.lower():
            raise ValueError("A hall with this name already exists.")

    hall = Hall(name, capacity, equipment, True)
    hall_repository.add(hall)

    return True
