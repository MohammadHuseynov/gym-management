from presentation import main_menu
from presentation.trainer_panel.workout_plans import workout_plan 
from presentation.trainer_panel.view_courses import view_course

def trainer_menu():

    print('-' * 8)
    print("1.View Courses")
    print("2.Manage Member Workout Plan")
    print("3.Return")

    while True:
        try:
            trainer_choice = int(input("Enter your choice: "))

        except:
            print("Please enter the number choice.")
            continue

        if trainer_choice == 1:
            view_course()

        elif trainer_choice == 2:
            workout_plan()

        elif trainer_choice == 3:
            return main_menu.main_menu()
        