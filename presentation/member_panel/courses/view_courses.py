from services.courses.get_courses import get_courses


def view_courses(course_repository):
    courses= get_courses(course_repository)
    active_courses=[]

    for course in courses:
        if course["is_active"]:
            active_courses.append(course)

    if not active_courses:
        print("No active courses found.")
        return

    print("\nActive Courses")
    print("----------")

    for number, course in enumerate(active_courses, 1):
        print(f"{number}.{course["title"]}")
        print("sport type:", course["sport_type"])
        print("Trainer", course["trainer"])
        print("Hall", course["hall"])
        print("Day:", course["day"])
        print("Time:", course["time"])
        print("Capacity:", course["capacity"])
        print("----------")