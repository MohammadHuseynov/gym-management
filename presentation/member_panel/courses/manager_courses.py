from presentation.member_panel.courses.view_courses import view_courses

def manage_course(course_repository, member):
    if course_repository is None:
        print("Course information is unavailable.")
        return

    while True:
        print("-" * 8)
        print("1.View Active Courses")
        print("2.Return")

        choice = input("Choose an option (1-2): ").strip()

        if choice == "1":
            view_courses(course_repository)
        elif choice == "2":
            return
        else:
            print("Please enter 1 or 2.")


