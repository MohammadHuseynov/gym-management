from services.courses.get_courses import get_courses
from services.courses.change_course_status import change_course_status


def activate_course(course_repository):
    title = input("Enter course title to activate (or 1 to go back): ").strip()

    if title == "1":
        return

    courses = get_courses(course_repository)
    selected_course = None

    for course in courses:
        if course["title"].lower() == title.lower():
            selected_course = course
            break

    if selected_course is None:
        print("Course not found.")
        return

    if selected_course["is_active"]:
        print("This course is already active.")
        return

    try:
        change_course_status(
            selected_course["title"],
            True,
            course_repository
        )
        print(f"Course {selected_course['title']} activated successfully.")

    except ValueError as error:
        print(error)
