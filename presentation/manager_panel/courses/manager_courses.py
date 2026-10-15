from presentation.manager_panel.courses.add_course import manage_add_course
from presentation.manager_panel.courses.edit_course import manage_edit_course
from presentation.manager_panel.courses.view_course import view_courses
from presentation.manager_panel.courses.manager_course_status import manage_course_status

def manage_courses(course_repository,user_repository,hall_repository):
    print("-" * 8)
    print("1.Add Course")
    print("2.Edit Course")
    print("3.Active\Deactive Course")
    print("4.View Course")  
    print("5.Return")

    
    users_choice = input("What you want to do?: ")
    

    if users_choice == "1":
        manage_add_course(course_repository,user_repository,hall_repository)

    elif users_choice == "2":
        manage_edit_course(course_repository,user_repository,hall_repository)

    elif users_choice == "3":
        manage_course_status(course_repository)

    elif users_choice == "4":
        view_courses(course_repository)

    elif users_choice == "5":
        return

    else:
        print("enter valid input")
    
