from services.users.get_users import get_users

def view_users(user_repository):
    users = get_users(user_repository)

    users_to_display = [user for user in users if user["role"].lower() in ("member", "trainer")]

    if not users_to_display:
        print("\nNo members or trainers found.")
        return

    print("-" * 8)
    print("ALL USERS")
    print("-" * 8)

    for user in users_to_display:
        print(f"Name: {user['name']}")
        print(f"Username: {user['username']}")
        print(f"Role: {user['role']}")
        print(f"Email: {user['email']}")
        print(f"Is Active: {user['is_active']}")
        print("-" * 60)

    print(f"Total users: {len(users_to_display)}")
    print("-" * 8)
