from presentation.manager_panel.halls.add_hall import add_hall
from presentation.manager_panel.halls.edit_hall import edit_hall
from presentation.manager_panel.halls.view_halls import view_halls
from presentation.manager_panel.halls.activate_hall import activate_hall

def manage_halls():
    print("-" * 8)
    print("1.Add Hall")
    print("2.Edit Hall")
    print("3.View Halls")
    print("4.Active\Deactive Hall")

    try:
        users_choice = int(input("What you want to do?: "))
    except:
        raise ValueError("please enter number choice")

    if users_choice == 1:
        add_hall()

    elif users_choice == 2:
        edit_hall()

    elif users_choice == 3:
        view_halls()

    elif users_choice == 4:
        activate_hall()