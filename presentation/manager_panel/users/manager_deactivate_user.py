
from services.users.get_users import get_users
from services.users.change_user_status import change_user_status


def deactivate_user(user_repository):
    username = input("Enter the username to deactivate (or 1 to go back): ").strip()

    if username.lower() == "1":
        return

    users = get_users(user_repository)

    selected_user = None

    for user in users:
        if (user["username"] == username and user["role"].lower() in ("member", "trainer")):
            selected_user = user
            break

    if selected_user is None:
        print("Member or trainer not found.")
        return

    if not selected_user["is_active"]:
        print("This user is already inactive.")
        return

    try:
        change_user_status(username, selected_user["role"], False, user_repository)
        print(f"{selected_user['name']} has been deactivated successfully.")

    except ValueError as error:
        print(error)
