class CourseRepository:
    def __init__(self, file_path="data/courses_data.txt"):
        self.file_path = file_path

    #region ADD
    def add(self, course):
        with open(self.file_path, "a", encoding="utf-8") as file:
            file.write(
                f"{course.title}|{course.sport_type}|{course.trainer}|{course.hall}|{course.day}|{course.time}|{course.capacity}|{course.is_active}\n"
            )
    #endregion

    #region UPDATE
    def update(self,old_title,title,sport_type,trainer,hall,day,time,capacity,is_active):
        with open(self.file_path, "r", encoding="utf-8") as file:
            lines = file.readlines()

        course_found = False
        updated_lines = []

        for line in lines:
            if not line.strip():
                continue

            fields = line.rstrip("\n").split("|")

            if len(fields) < 8:
                updated_lines.append(line)
                continue

            if fields[0] == old_title:
                fields[0] = title
                fields[1] = sport_type
                fields[2] = trainer
                fields[3] = hall
                fields[4] = day
                fields[5] = time
                fields[6] = str(capacity)
                fields[7] = str(is_active)
                course_found = True

            updated_lines.append("|".join(fields) + "\n")

        if not course_found:
            return False

        with open(self.file_path, "w", encoding="utf-8") as file:
            file.writelines(updated_lines)

        return True
    #endregion

    #region GET_ALL
    def get_all(self):
        courses = []

        with open(self.file_path, "r", encoding="utf-8") as file:
            for line in file:
                if not line.strip():
                    continue

                fields = line.rstrip("\n").split("|")

                if len(fields) < 8:
                    continue

                courses.append({
                    "title": fields[0],
                    "sport_type": fields[1],
                    "trainer": fields[2],
                    "hall": fields[3],
                    "day": fields[4],
                    "time": fields[5],
                    "capacity": fields[6],
                    "is_active": fields[7] == "True"
                })

        return courses
    #endregion

    #region CHANGE STATUS
    def update_status(self, title, is_active):
        with open(self.file_path, "r", encoding="utf-8") as file:
            lines = file.readlines()

        course_found = False
        updated_lines = []

        for line in lines:
            if not line.strip():
                continue

            fields = line.rstrip("\n").split("|")

            if len(fields) < 8:
                updated_lines.append(line)
                continue

            if fields[0] == title:
                fields[7] = str(is_active)
                course_found = True

            updated_lines.append("|".join(fields) + "\n")

        if not course_found:
            return False

        with open(self.file_path, "w", encoding="utf-8") as file:
            file.writelines(updated_lines)

        return True
    #endregion
