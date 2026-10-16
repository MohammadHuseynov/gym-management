def handle_login(user_repository, expected_role):
    if expected_role == "manager":
       
        username = input("Enter manager username (or 1 to go back): ").strip()

        if username == "1":
            return 

        password = input("Enter manager password (or 1 to go back): ").strip()


        if username == "1":
            return 


        if username == "Admin" and password == "1234":
            print("Welcome, Admin!")
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
