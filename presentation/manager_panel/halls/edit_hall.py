
from services.halls.get_halls import get_halls
from services.halls.edit_hall import edit_hall


def manage_edit_hall(hall_repository):
    old_name = input("Enter the name of the hall to edit (or 1 to go back): ").strip()

    if old_name == "1":
        return False

    halls = get_halls(hall_repository)

    selected_hall = None

    for hall in halls:
        if hall["name"].lower() == old_name.lower():
            selected_hall = hall
            break

    if selected_hall is None:
        print("Hall not found.")
        return False


    while True:
        name = input("Enter new hall name: ").strip()

        if not name:
            print("Hall name cannot be empty.")
            continue

        if name.lower() != selected_hall["name"].lower():
            duplicate = any(hall["name"].lower() == name.lower()for hall in halls)

            if duplicate:
                print("Hall name already exists. Try another.")
                continue

        break

    while True:
        capacity_input = input("Enter new hall capacity: ").strip()

        try:
            capacity = int(capacity_input)

            if capacity <= 0:
                print("Capacity must be greater than zero.")
                continue

            break

        except ValueError:
            print("Capacity must be a valid number.")

    while True:
        equipment = input("Enter new hall equipment: ").strip()

        if equipment:
            break

        print("Equipment cannot be empty.")

    
    current_status = selected_hall["is_active"]
    status_text = "Active" if current_status else "Inactive"

    print(f"Current status: {status_text}")
    print("1. Active")
    print("2. Inactive")

    while True:
        status_choice = input("Enter new status (1-2): ").strip()

        if status_choice == "1":
            is_active = True
            break

        elif status_choice == "2":
            is_active = False
            break

        print("Invalid choice. Please enter 1 or 2.")

    try:
        edit_hall(
            selected_hall["name"],
            name,
            capacity,
            equipment,
            is_active,
            hall_repository
        )

        print("Hall updated successfully!")
        return True

    except ValueError as error:
        print(f"Error: {error}")
        return False
