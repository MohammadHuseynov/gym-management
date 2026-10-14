from presentation.manager_panel.users.manager_users_menu import manager_users
from presentation.manager_panel.halls.manager_halls import manage_halls
from presentation.manager_panel.courses.manager_courses import manage_courses
from presentation.manager_panel.reports.manager_reports import manage_report

def manager_menu():  
    while True:

        print('-' * 8)
        print("1.Managing Users")
        print("2.Managing Halls")
        print("3.Managing Courses")
        print("4.Managing Subscriptions")
        print("5.View Reports")
        print("6.Return")
    
        try:
            manager_choice = int(input("Enter the number you want to do: "))
        except ValueError:
            print("Please enter the number choice.")
            continue
        
        if manager_choice == 1:
            manager_users()

        elif manager_choice == 2:
            manage_halls()

        elif manager_choice == 3:
            manage_courses()

        elif manager_choice == 4:
            print("**SUBSCRIPTION MUST BE ADDED**")

        elif manager_choice == 5:
            manage_report()

        elif manager_choice == 6:
            return

        
