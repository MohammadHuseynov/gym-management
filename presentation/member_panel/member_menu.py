from presentation.member_panel.view_subscription_status import view_subscription_status
from presentation.member_panel.view_subscription_plans import view_subscription_plans
from presentation.member_panel.wallet.manager_wallet import manage_wallet
from presentation.member_panel.courses.manager_courses import manage_course
from presentation.member_panel.workout_plan import view_workout_plan

def member_menu(member, user_repository, subscription_repository, course_repository, workout_repository):
    while True:
        print("-" * 8)
        print("1.Available Subscription Plans")
        print("2.Subscription Status")
        print("3.Wallet")
        print("4.Courses")
        print("5.View Workout Plan")
        print("6.Return")

        user_choice = input("please enter a number choice: ")

    
        if user_choice == "1":
            view_subscription_plans(subscription_repository)

        elif user_choice == "2":
            view_subscription_status(member, subscription_repository)

        elif user_choice == "3":
            manage_wallet()

        elif user_choice == "4":
            manage_course(course_repository, member)

        elif user_choice == "5":
            view_workout_plan(member, workout_repository)

        elif user_choice == "6":
            return

        else:
            print("please enter correctly")
