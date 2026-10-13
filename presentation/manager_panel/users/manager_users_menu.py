from presentation.manager_panel.users.manager_add_user import manage_add_user

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

