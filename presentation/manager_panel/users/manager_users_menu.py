from presentation.manager_panel.users.manager_add_user import manage_add_user
from presentation.manager_panel.users.manager_edit_user import manage_edit_user
from presentation.manager_panel.users.manager_change_user_status import manage_change_status
from presentation.manager_panel.users.view_users import view_users

def manager_users(user_repository):
    print('-' * 8)
    print("1.Add User")    
    print("2.Edit User")
    print("3.Active or Deactive User")
    print("4.View All Users")
    print("5.Return")

    users_choice = input("the user type: ")
    
    if users_choice == "1":
        manage_add_user(user_repository)

    elif users_choice == "2":
        manage_edit_user(user_repository)

    elif users_choice == "3":
        manage_change_status(user_repository)

    elif users_choice == "4":
        view_users(user_repository)

    elif users_choice == "5":
        return

    else:
        print("please enter correctly")




