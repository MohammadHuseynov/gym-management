
from model.course import Course


def add_course(title,sport_type,trainer,hall,day,time,capacity,course_repository,user_repository,hall_repository):
    title = title.strip()
    sport_type = sport_type.strip()
    trainer = trainer.strip()
    hall = hall.strip()
    day = day.strip()
    time = time.strip()

    if not title:
        raise ValueError("Course title cannot be empty.")

    if not sport_type:
        raise ValueError("Sport type cannot be empty.")

    if not trainer:
        raise ValueError("Trainer name cannot be empty.")

    if not hall:
        raise ValueError("Hall name cannot be empty.")

    if not day:
        raise ValueError("Day cannot be empty.")

    if not time:
        raise ValueError("Time cannot be empty.")

    try:
        capacity = int(capacity)
    except (ValueError, TypeError):
        raise ValueError("Capacity must be a number.")

    if capacity <= 0:
        raise ValueError("Capacity must be greater than zero.")

    
    courses = course_repository.get_all()

    for course in courses:
        if course["title"].lower() == title.lower():
            raise ValueError("A course with this title already exists.")

    
    users = user_repository.get_all()

    selected_trainer = None

    for user in users:
        if (user["name"].lower() == trainer.lower()and user["role"].lower() == "trainer"):
            selected_trainer = user
            break

    if selected_trainer is None:
        raise ValueError("Trainer not found.")

    if not selected_trainer["is_active"]:
        raise ValueError("The selected trainer is inactive.")

    
    halls = hall_repository.get_all()

    selected_hall = None

    for existing_hall in halls:
        if existing_hall["name"].lower() == hall.lower():
            selected_hall = existing_hall
            break

    if selected_hall is None:
        raise ValueError("Hall not found.")

    if not selected_hall["is_active"]:
        raise ValueError("The selected hall is inactive.")

    course = Course(title,sport_type,selected_trainer["name"],selected_hall["name"],day,time,capacity,True)

    course_repository.add(course)

    return True
