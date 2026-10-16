from services.courses.edit_course import edit_course
from services.courses.get_courses import get_courses


def manage_edit_course(course_repository,user_repository,hall_repository):
    old_title = input("Enter course title to edit (or 1 to go back): ").strip()

    if old_title == "1":
        return False

    courses = get_courses(course_repository)
    selected_course = None

    for course in courses:
        if course["title"].lower() == old_title.lower():
            selected_course = course
            break

    if selected_course is None:
        print("Course not found.")
        return False

    title = input("Enter new course title: ").strip()
    sport_type = input("Enter new sport type: ").strip()
    trainer = input("Enter new trainer name: ").strip()
    hall = input("Enter new hall name: ").strip()
    day = input("Enter new course day: ").strip()
    time = input("Enter new course time: ").strip()

    while True:
        capacity = input("Enter new course capacity: ").strip()

        try:
            if int(capacity) <= 0:
                print("Capacity must be greater than zero.")
                continue
            break
        except ValueError:
            print("Capacity must be a valid number.")

    print("Select course status:")
    print("1. Active")
    print("2. Inactive")

    while True:
        status_choice = input("Choose (1-2): ").strip()

        if status_choice == "1":
            is_active = True
            break
        elif status_choice == "2":
            is_active = False
            break
        else:
            print("Invalid choice. Enter 1 or 2.")

    try:
        edit_course(
            old_title,
            title,
            sport_type,
            trainer,
            hall,
            day,
            time,
            capacity,
            is_active,
            course_repository,
            user_repository,
            hall_repository
        )

        print("Course updated successfully!")
        return True

    except ValueError as error:
        print(f"Error: {error}")
        return False
