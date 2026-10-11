def manage_users_manu():
    print("1.Add User")    
    print("2.Edit User")
    print("3.Active\Deactive User")
    print("4.View All Users")

    try:
        users_choice = int(input("the user type: "))
    except:
        raise ValueError("please enter number choice")
    if users_choice == 1:
        print("calls the def trainer")