def manage_report():
    print("-" * 8)
    print("1.Active User Count Report")
    print("2.Active Trainer Count Report")
    print("3.Active Courses Count Report")
    print("4.Full Income Report")

    try: 
        user_choice = int(input("which action you want to do? "))
    except:
        raise ValueError("please enter a number")

    if user_choice == 1:
        print("a service logic for active user count")

    elif user_choice == 2:
        print("a service logic for active trainer count")
    
    elif user_choice == 3:
        print("a service logic for active courses count")

    elif user_choice == 4:
        print("a service logic for full income")