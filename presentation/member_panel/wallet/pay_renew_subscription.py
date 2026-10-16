def pay_renew_subscription():
    print("-" * 8)
    print("1.One Month")
    print("2.Three Month")
    print("3.Six Month")
    print("4.Return")

    
    user_choice = input("please enter your choice: ")


    if user_choice == "1":
        print("add 1 month if enough money")

    elif user_choice == "2":
        print("add 3 month if enough money")

    elif user_choice == "3":
        print("add 6 month if enough money")

    elif user_choice == "4":
        return

    else:
        print("please enter correctly")
