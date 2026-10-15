from presentation.manager_panel.users.manager_activate_user import activate_user
from presentation.manager_panel.users.manager_deactivate_user import deactivate_user


def manage_change_status(user_repository):

    while True:
        print("-" * 8)
        print("1.Activate Users")
        print("2.Deactivate Users")
        print("3.Return")


        user_choice = input("Enter what you want to do (1-3): ")

        if user_choice == "1":
            activate_user(user_repository)

        elif user_choice == "2":
            deactivate_user(user_repository)

        elif user_choice == "3":
            return

        else:
            print("please enter correct input")


    