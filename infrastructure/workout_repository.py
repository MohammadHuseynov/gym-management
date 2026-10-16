
class WorkoutRepository:
    def __init__(self, file_path="data/workout_plans_data.txt"):
        self.file_path = file_path

    #region ADD
    def add(self, member_username, course_title, exercises):
        with open(self.file_path, "a", encoding="utf-8") as file:
            for exercise in exercises:
                file.write(f"{member_username}|{course_title}|{exercise.name}|{exercise.sets}|{exercise.reps}|{exercise.rest_time}|{exercise.description}\n")
    #endregion

    #region GET_ALL
    def get_all(self):
        workout_plans = []

        with open(self.file_path, "r", encoding="utf-8") as file:
            for line in file:
                if not line.strip():
                    continue

                fields = line.rstrip("\n").split("|")

                if len(fields) < 7:
                    continue

                workout_plans.append({
                    "member_username": fields[0],
                    "course_title": fields[1],
                    "exercise": {
                        "name": fields[2],
                        "sets": int(fields[3]),
                        "reps": int(fields[4]),
                        "rest_time": fields[5],
                        "description": fields[6]
                    }
                })

        return workout_plans
    #endregion
