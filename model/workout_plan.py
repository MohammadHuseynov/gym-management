class Exercise:
    def __init__(self, name, sets, reps, rest_time, description):
        self.name = name
        self.sets = sets
        self.reps = reps
        self.rest_time = rest_time
        self.description = description


class WorkoutPlan:
    def __init__(self, member, course):
        self.member = member
        self.course = course
        self.exercises = []