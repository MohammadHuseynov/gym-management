from services.halls.add_hall import add_hall


def manage_add_hall(hall_repository):

    name = input("Enter hall name (or 1 to go back): ").strip()

    if name == "1":
        return

    capacity = input("Enter hall capacity: ").strip()
    equipment = input("Enter hall equipment: ").strip()

    try:
        add_hall(name, capacity, equipment, hall_repository)
        print("Hall added successfully!")

    except ValueError as error:
        print(error)
