from presentation.manager_panel.courses.activate_course import activate_course
from presentation.manager_panel.courses.deactivate_course import deactivate_course


def manage_course_status(course_repository):

    while True:
        print("-" * 8)
        print("1.Activate Course")
        print("2.Deactivate Course")
        print("3.Return")


        user_choice = input("Enter what you want to do (1-3): ")

        if user_choice == "1":
            activate_course(course_repository)

        elif user_choice == "2":
            deactivate_course(course_repository)

        elif user_choice == "3":
            return

        else:
            print("please enter correct input")


    