from services.halls.get_halls import get_halls
from services.halls.change_hall_status import change_hall_status


def deactivate_hall(hall_repository):
    name = input("Enter the hall name to deactivate (or 1 to go back): ").strip()

    if name == "1":
        return

    halls = get_halls(hall_repository)

    selected_hall = None

    for hall in halls:
        if hall["name"].lower() == name.lower():
            selected_hall = hall
            break

    if selected_hall is None:
        print("Hall not found.")
        return

    if not selected_hall["is_active"]:
        print("This hall is already inactive.")
        return

    try:
        change_hall_status(selected_hall["name"],False,hall_repository)
        print(f"Hall {selected_hall["name"]} has been deactivated successfully.")

    except ValueError as error:
        print(error)