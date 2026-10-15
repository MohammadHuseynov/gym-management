from services.halls.get_halls import get_halls


def view_halls(hall_repository):
    halls = get_halls(hall_repository)

    if not halls:
        print("No halls found.")
        return

    print("-" * 8)
    print("ALL HALLS")
    print("-" * 8)

    for hall in halls:
        print(f"Name: {hall['name']}")
        print(f"Capacity: {hall['capacity']}")
        print(f"Equipment: {hall['equipment']}")
        print(f"Is Active: {hall['is_active']}")
        print("-" * 8)

    print(f"Total halls: {len(halls)}")
    print("-" * 8)
