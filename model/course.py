class Course:
    def __init__(self, title, sport_type, trainer, hall, day, time, capacity, is_active=True):
        self.title = title
        self.sport_type = sport_type
        self.trainer = trainer
        self.hall = hall
        self.day = day
        self.time = time
        self.capacity = capacity
        self.is_active = is_active

        self.enrolled_members = []

#sport_type means yoga fitness bodybuilding and etc