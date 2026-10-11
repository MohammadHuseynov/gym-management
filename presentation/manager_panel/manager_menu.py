import main_menu
from users import manage_users_menu


def manager_menu():  
    print("1.Managing Users")
    print("2.Managing Halls")
    print("3.Managing Courses")
    print("4.Managing Subscriptions")
    print("5.View Reports")
    print("6.Return")


    while True:
        try:
            manager_choice = int(input("Enter the number you want to do: "))
        except ValueError:
            print("Please enter the number choice.")
            continue
        
        if manager_choice == 1:
            manage_users_menu.manage_users_manu()

        elif manager_choice == 2:
            print("go to the halls folder and show manager what he want to do")

        elif manager_choice == 3:
            print("go to the courses folder and show manager what he want to do")

        elif manager_choice == 4:
            print("go to the subscriptions folder and show manager what he want to do")

        elif manager_choice == 5:
            print("go to the reports folder and show manager what he want to do")

        elif manager_choice == 6:
            return main_menu.main_menu()
