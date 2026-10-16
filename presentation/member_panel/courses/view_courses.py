from services.courses.get_courses import get_courses


def view_courses(course_repository):
    courses = [
        course for course in get_courses(course_repository)
        if course["is_active"]
    ]

    if not courses:
        print("There are no active courses right now.")
        return

    print("-" * 8)
    print("ACTIVE COURSES")
    print("-" * 8)

    for number, course in enumerate(courses, start=1):
        print(f"{number}. {course['title']}")
        print(f"Sport: {course['sport_type']}")
        print(f"Trainer: {course['trainer']}")
        print(f"Hall: {course['hall']}")
        print(f"Day and time: {course['day']} at {course['time']}")
        print(f"Capacity: {course['capacity']}")
        print("-" * 8)

    print(f"Total active courses: {len(courses)}")
