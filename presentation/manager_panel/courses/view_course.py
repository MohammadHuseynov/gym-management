from services.courses.get_courses import get_courses


def view_courses(course_repository):
    courses = get_courses(course_repository)

    if not courses:
        print("No courses found.")
        return

    print("-" * 8)
    print("ALL COURSES")
    print("-" * 8)

    for course in courses:
        print(f"Title: {course['title']}")
        print(f"Sport Type: {course['sport_type']}")
        print(f"Trainer: {course['trainer']}")
        print(f"Hall: {course['hall']}")
        print(f"Day: {course['day']}")
        print(f"Time: {course['time']}")
        print(f"Capacity: {course['capacity']}")
        print(f"Is Active: {course['is_active']}")
        print("-" * 8)

    print(f"Total courses: {len(courses)}")
