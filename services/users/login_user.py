admin_username = None
admin_password = None
def handle_login(user_repository, expected_role):
    if expected_role == "manager":
       
        username = input("Enter manager username (or 1 to go back): ").strip()

        if username == "1":
            return 

        password = input("Enter manager password (or 1 to go back): ").strip()


        if password == "1":
            return 

        with open("data/seed_data.txt", "r", encoding="utf-8") as file:
            lines = file.readlines()

        for line in lines:
            line = line.strip()
            if not line or "=" not in line:
                continue

            key, value = line.split("=")
            key = key.strip()
            value = value.strip()

            if key == "username":
                admin_username = value
            elif key == "password":
                admin_password = value

        if username == admin_username and password == admin_password:
            print(f"Welcome, {admin_username}!")
            return {"name": "Admin", "role": "manager"}

        print("Incorrect username or password.")
        return None

    username = input("Enter username (or 1 to go back): ").strip()

    if username.lower() == "1":
        return None

    password = input("Enter password: ")

    users = user_repository.get_all()

    for user in users:
        if (user["username"] == username and user["role"].lower() == expected_role.lower()):
            if not user["is_active"]:
                print("This account is inactive.")
                return None

            if user["password"] == password:
                print(f"Welcome, {user['name']}!")
                return user

            print("Incorrect username or password.")
            return None

    print("Incorrect username or password.")
    return None
