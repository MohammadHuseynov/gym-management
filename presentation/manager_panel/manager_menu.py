from presentation.manager_panel.users.manager_users_menu import manager_users
from presentation.manager_panel.halls.manager_halls import manage_halls
from presentation.manager_panel.courses.manager_courses import manage_courses
from presentation.manager_panel.reports.manager_reports import manage_report
from presentation.manager_panel.subscriptions.manage_subscription import manage_subscription


def manager_menu(user_repository, hall_repository, course_repository):  
    while True:

        print('-' * 8)
        print("1.Managing Users")
        print("2.Managing Halls")
        print("3.Managing Courses")
        print("4.Managing Subscriptions")
        print("5.View Reports")
        print("6.Return")

        manager_choice = input("Enter the number you want to do: ")

        if manager_choice == "1":
            manager_users(user_repository)

        elif manager_choice == "2":
            manage_halls(hall_repository)

        elif manager_choice == "3":
            manage_courses(course_repository,user_repository,hall_repository)

        elif manager_choice == "4":
            manage_subscription(user_repository, subscription_repository)

        elif manager_choice == "5":
            manage_report(user_repository, course_repository)

        elif manager_choice == "6":
            return

        else:
            print("enter number correctly")




        
