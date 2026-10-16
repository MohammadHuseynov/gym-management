def change_course_status(title, is_active, course_repository):
    courses = course_repository.get_all()
    selected_course = None

    for course in courses:
        if course["title"].lower() == title.lower():
            selected_course = course
            break

    if selected_course is None:
        raise ValueError("Course not found.")

    if selected_course["is_active"] == is_active:
        status = "active" if is_active else "inactive"
        raise ValueError(f"This course is already {status}.")

    updated = course_repository.update_status(
        selected_course["title"],
        is_active
    )

    if not updated:
        raise ValueError("Could not update course status.")

    return True
