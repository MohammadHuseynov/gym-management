def edit_course(old_title,title,sport_type,trainer,hall,day,time,capacity,is_active,course_repository,user_repository,hall_repository):
    courses = course_repository.get_all()
    selected_course = None

    for course in courses:
        if course["title"].lower() == old_title.lower():
            selected_course = course
            break

    if selected_course is None:
        raise ValueError("Course not found.")

    title = title.strip()
    sport_type = sport_type.strip()
    trainer = trainer.strip()
    hall = hall.strip()
    day = day.strip()
    time = time.strip()

    if not all([title, sport_type, trainer, hall, day, time]):
        raise ValueError("All course fields must be filled in.")

    try:
        capacity = int(capacity)
    except (ValueError, TypeError):
        raise ValueError("Capacity must be a number.")

    if capacity <= 0:
        raise ValueError("Capacity must be greater than zero.")

    for course in courses:
        if (course["title"].lower() == title.lower()and course["title"].lower() != old_title.lower()):
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

    updated = course_repository.update(
        selected_course["title"],
        title,
        sport_type,
        selected_trainer["name"],
        selected_hall["name"],
        day,
        time,
        capacity,
        is_active
    )

    if not updated:
        raise ValueError("Could not update course.")

    return True
