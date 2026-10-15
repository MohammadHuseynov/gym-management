def active_members(user_repository):
    users = user_repository.get_all()

    count = 0

    for user in users:
        if user["role"].lower() == "member" and user["is_active"]:
            count += 1

    print(f"Active Members: {count}")
