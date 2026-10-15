from presentation import main_menu
from presentation.trainer_panel.workout_plans import workout_plan 
from presentation.trainer_panel.view_courses import view_course

def trainer_menu(trainer, user_repository, course_repository,workout_repository):
    while True:
        print('-' * 8)
        print("1.View Courses")
        print("2.Manage Member Workout Plan")
        print("3.Return")
    
    
        trainer_choice = input("Enter your choice: ")
    
            
        if trainer_choice == "1":
            view_course(trainer, course_repository)

        elif trainer_choice == "2":
            workout_plan(trainer,user_repository,course_repository,workout_repository)

        elif trainer_choice == "3":
            return main_menu.main_menu()
        
        else: 
            print("please enter correctly")
        