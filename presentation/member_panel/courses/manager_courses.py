from presentation.member_panel.courses.view_courses import view_courses
from presentation.member_panel.courses.enroll_course import enroll_course
from presentation.member_panel.courses.quit_course import quit_course


def manage_course(course_repository):
    while True:
        print("1. View Active Courses")
        print("2. Enroll in Course")
        print("3. Quit Course")
        print("0. Return")

        user_choice=input("inter your choice: ").strip()

        if user_choice == "1":
            view_courses(course_repository)
        elif user_choice == "2":
            enroll_course()
        elif user_choice == "3":
            quit_course()
        elif user_choice == "0":
            return
        else:
            print("Invalid choice.")