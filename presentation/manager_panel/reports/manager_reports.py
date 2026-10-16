from presentation.manager_panel.reports.active_members_report import active_members
from presentation.manager_panel.reports.active_trainers_report import active_trainers
from presentation.manager_panel.reports.active_courses_report import active_courses
from presentation.manager_panel.reports.income_report import income_report


def manage_report(user_repository, course_repository):
    while True:
        print("-" * 8)
        print("1.Active Member Count Report")
        print("2.Active Trainer Count Report")
        print("3.Active Courses Count Report")
        print("4.Full Income Report")
        print("5.Return")
    
     
        user_choice = input("which action you want to do? ")
    
    
        if user_choice == "1":
            active_members(user_repository)
    
        elif user_choice == "2":
            active_trainers(user_repository)
        
        elif user_choice == "3":
            active_courses(course_repository)
    
        elif user_choice == "4":
            income_report()

        elif user_choice == "5":
            return
    
        else:
            print("please enter valid number choice (1-4)")