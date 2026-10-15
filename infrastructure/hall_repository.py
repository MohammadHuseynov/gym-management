
class HallRepository:
    def __init__(self, file_path="data/halls_data.txt"):
        self.file_path = file_path

#region ADD
    def add(self, hall):
        with open(self.file_path, "a", encoding="utf-8") as file:
            file.write(f"{hall.name}|{hall.capacity}|{hall.equipment}|{hall.is_active}\n")
#endregion

#region UPDATE
    def update(self, old_name, name, capacity, equipment, is_active):
        with open(self.file_path, "r", encoding="utf-8") as file:
            lines = file.readlines()

        hall_found = False
        updated_lines = []

        for line in lines:
            if not line.strip():
                continue

            fields = line.rstrip("\n").split("|")

            if len(fields) < 4:
                updated_lines.append(line)
                continue

            if fields[0] == old_name:
                fields[0] = name
                fields[1] = str(capacity)
                fields[2] = equipment
                fields[3] = str(is_active)
                hall_found = True

            updated_lines.append("|".join(fields) + "\n")

        if not hall_found:
            return False

        with open(self.file_path, "w", encoding="utf-8") as file:
            file.writelines(updated_lines)

        return True
#endregion

#region GET_ALL
    def get_all(self):
        halls = []

        with open(self.file_path, "r", encoding="utf-8") as file:
            for line in file:
                if not line.strip():
                    continue

                fields = line.rstrip("\n").split("|")

                if len(fields) < 4:
                    continue

                halls.append({
                    "name": fields[0],
                    "capacity": fields[1],
                    "equipment": fields[2],
                    "is_active": fields[3] == "True"
                })

        return halls
#endregion

#region CHANGE STATUS
    def update_status(self, name, is_active):
        with open(self.file_path, "r", encoding="utf-8") as file:
            lines = file.readlines()

        hall_found = False
        updated_lines = []

        for line in lines:
            if not line.strip():
                continue

            fields = line.rstrip("\n").split("|")

            if len(fields) < 4:
                updated_lines.append(line)
                continue

            if fields[0] == name:
                fields[3] = str(is_active)
                hall_found = True

            updated_lines.append("|".join(fields) + "\n")

        if not hall_found:
            return False

        with open(self.file_path, "w", encoding="utf-8") as file:
            file.writelines(updated_lines)

        return True
#endregion
