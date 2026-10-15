
from services.courses.get_courses import get_courses
from services.courses.change_course_status import change_course_status


def deactivate_course(course_repository):
    title = input("Enter course title to deactivate (or 1 to go back): ").strip()

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

    if not selected_course["is_active"]:
        print("This course is already inactive.")
        return

    try:
        change_course_status(
            selected_course["title"],
            False,
            course_repository
        )
        print(f"Course {selected_course['title']} deactivated successfully.")

    except ValueError as error:
        print(error)
