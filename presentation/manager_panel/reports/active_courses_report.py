def active_courses(course_repository):
    courses = course_repository.get_all()

    count = 0

    for course in courses:
        if course["is_active"]:
            count += 1

    print(f"Active Courses: {count}")
