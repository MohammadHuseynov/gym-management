from pathlib import Path


class UserRepository:
    def __init__(self, file_path="data/users_data.txt"):
        self.file_path = Path(file_path)
        self.file_path.parent.mkdir(parents=True, exist_ok=True)
        self.file_path.touch(exist_ok=True)

#region ADD
    def add(self, user):
        with open(self.file_path, "a", encoding="utf-8") as file:
            file.write(
                f"{user.name}|{user.username}|{user.password}|"
                f"{user.email}|{user.role}|{user.is_active}\n"
            )
#endregion

#region UPDATE
    def update(self, old_username, name, username, password, email):
        with open(self.file_path, "r", encoding="utf-8") as file:
            lines = file.readlines()

        user_found = False
        updated_lines = []

        for line in lines:
            if not line.strip():
                continue

            fields = line.rstrip("\n").split("|")

            if len(fields) < 6:
                updated_lines.append(line)
                continue

            if fields[1] == old_username:
                fields[0] = name
                fields[1] = username
                fields[2] = password
                fields[3] = email
                user_found = True

            updated_lines.append("|".join(fields) + "\n")

        if not user_found:
            return False

        with open(self.file_path, "w", encoding="utf-8") as file:
            file.writelines(updated_lines)

        return True
#endregion

#region GET_ALL
    def get_all(self):
        users = []

        with open(self.file_path, "r", encoding="utf-8") as file:
            for line in file:
                if not line.strip():
                    continue

                fields = line.rstrip("\n").split("|")

                users.append({
                    "name": fields[0],
                    "username": fields[1],
                    "password": fields[2],
                    "email": fields[3],
                    "role": fields[4],
                    "is_active": fields[5] == "True"
                })

        return users
#endregion
    

#region CHANGE STATUS
    def update_status(self, username, role, is_active):
        with open(self.file_path, "r", encoding="utf-8") as file:
            lines = file.readlines()

        user_found = False
        updated_lines = []

        for line in lines:
            if not line.strip():
                continue

            fields = line.rstrip("\n").split("|")

            if len(fields) < 6:
                updated_lines.append(line)
                continue

            if fields[1] == username and fields[4] == role:
                fields[5] = str(is_active)
                user_found = True

            updated_lines.append("|".join(fields) + "\n")

        if not user_found:
            return False

        with open(self.file_path, "w", encoding="utf-8") as file:
            file.writelines(updated_lines)

        return True
#endregion
    
    def is_username_unique(self, username):
        with open(self.file_path, "r", encoding="utf-8") as file:
            for line in file:
                if not line.strip():
                    continue
                
                fields = line.rstrip("\n").split("|")
    
                if len(fields) >= 6 and fields[1] == username:
                    return False
    
        return True

