from services.courses.get_courses import get_courses
from services.courses.enroll_member import enroll_member , get_enrollments

def enroll_course(course_repository):
    while True:
        courses= get_courses(course_repository)
        available_courses = []
    for course in courses:
        enrolled_count = 0

        for enrollment in enrollments:
            if enrollment["course_title"] == course["title"]:
                if enrollment["status"] == "active":
                    enrolled_count += 1

        remaining = int(course["capacity"]) - enrolled_count

        if course["is_active"] and remaining > 0 :
            available_courses.append(course)

    print("\n Available Courses")

    if not available_courses:
        print(" no available courses. ")
        return

    for number, course in enumerate(available_courses, 1):
        print(f"\n{number}. {course["title"]}")
        print("Sport Type:", course["sport_type"])
        print("Trainer:", course["trainer"])
        print("Hall:", course["hall"])
        print("Day:", course["day"])
        print("Time:", course["time"])

    print("\n0. Return")
    if input("Choose an option: ") == "0":
        return
        print("Invalid choice.") 