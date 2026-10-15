from presentation.member_panel.view_subscription_status import view_subscription_status
from presentation.member_panel.wallet.manager_wallet import manage_wallet
from presentation.member_panel.courses.manager_courses import manage_course
from presentation.member_panel.workout_plan import view_workout_plan

def member_menu():
    while True:
        print("-" * 8)
        print("1.Subscription Status")
        print("2.Wallet")
        print("3.Courses")
        print("4.Workout Plan")
        print("5.Return")

        user_choice = input("please enter a number choice: ")

    
        if user_choice == 1:
            view_subscription_status()

        elif user_choice == 2:
            manage_wallet()

        elif user_choice == 3:
            manage_course()

        elif user_choice == 4:
            view_workout_plan()

        elif user_choice == 5:
            return
