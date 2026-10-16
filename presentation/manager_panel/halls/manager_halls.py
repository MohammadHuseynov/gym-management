from presentation.manager_panel.halls.add_hall import manage_add_hall
from presentation.manager_panel.halls.edit_hall import manage_edit_hall
from presentation.manager_panel.halls.view_halls import view_halls
from presentation.manager_panel.halls.manager_halls_status import manage_hall_status

def manage_halls(hall_repository):
    print("-" * 8)
    print("1.Add Hall")
    print("2.Edit Hall")
    print("3.Active or Deactive Hall")
    print("4.View Halls")
    print("5.Return")

    
    users_choice = input("What you want to do?: ")
    

    if users_choice == "1":
        manage_add_hall(hall_repository)

    elif users_choice == "2":
        manage_edit_hall(hall_repository)

    elif users_choice == "3":
        manage_hall_status(hall_repository)

    elif users_choice == "4":
        view_halls(hall_repository)

    elif users_choice == "5":
        return

    else:
        print("please enter correctly")