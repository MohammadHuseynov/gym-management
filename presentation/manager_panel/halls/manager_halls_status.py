from presentation.manager_panel.halls.activate_hall import activate_hall
from presentation.manager_panel.halls.deactivate_hall import deactivate_hall


def manage_hall_status(hall_repository):

    while True:
        print("-" * 8)
        print("1.Activate Halls")
        print("2.Deactivate Halls")
        print("3.Return")


        user_choice = input("Enter what you want to do (1-3): ")

        if user_choice == "1":
            activate_hall(hall_repository)

        elif user_choice == "2":
            deactivate_hall(hall_repository)

        elif user_choice == "3":
            return

        else:
            print("please enter correct input")


    