from presentation.manager_panel.users.manager_add_user import manage_add_user
from presentation.manager_panel.users.manager_edit_user import manage_edit_user
from presentation.manager_panel.users.manager_change_user_status import manage_change_status
from presentation.manager_panel.users.view_users import view_users

def manager_users():
    print('-' * 8)
    print("1.Add User")    
    print("2.Edit User")
    print("3.Active\Deactive User")
    print("4.View All Users")

    try:
        users_choice = int(input("the user type: "))
    except:
        raise ValueError("please enter number choice")
    
    if users_choice == 1:
        manage_add_user()

    elif users_choice == 2:
        manage_edit_user()

    elif users_choice == 3:
        manage_change_status()

    elif users_choice == 4:
        view_users()




