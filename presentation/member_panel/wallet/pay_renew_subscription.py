def pay_renew_subscription():
    print("-" * 8)
    print("1.One Month")
    print("2.Three Month")
    print("3.Six Month")

    try:
        user_choice = int(input("please enter your choice: "))
    except:
        raise ValueError("please enter a number")


    if user_choice == 1:
        print("add 1 month if enough money")

    elif user_choice == 2:
        print("add 3 month if enough money")

    elif user_choice == 3:
        print("add 6 month if enough money")