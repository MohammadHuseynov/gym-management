from services.users.get_users import get_users

def view_users(user_repository):
    users = get_users(user_repository)

    active_users = [user for user in users if user["is_active"] and user["role"].lower() in ("member", "trainer")]

    if not active_users:
        print("\nNo active members or trainers found.")
        return

    print("\nActive Users:")

    for user in active_users:
        print("-" * 8)
        print(f"Name: {user['name']}")
        print(f"Username: {user['username']}")
        print(f"Email: {user['email']}")
        print(f"Role: {user['role']}")
        print(f"Status: {'Active' if user['is_active'] else 'Inactive'}")

    