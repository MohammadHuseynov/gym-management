from presentation.manager_panel.courses.add_course import add_course
from presentation.manager_panel.courses.edit_course import edit_course
from presentation.manager_panel.courses.view_course import view_courses
from presentation.manager_panel.courses.activate_course import activate_course

def manage_courses():
    print("-" * 8)
    print("1.Add Course")
    print("2.Edit Course")
    print("3.View Course")
    print("4.Active\Deactive Course")

    try:
        users_choice = int(input("What you want to do?: "))
    except:
        raise ValueError("please enter number choice")

    if users_choice == 1:
        add_course()

    elif users_choice == 2:
        edit_course()

    elif users_choice == 3:
        view_courses()

    elif users_choice == 4:
        activate_course()