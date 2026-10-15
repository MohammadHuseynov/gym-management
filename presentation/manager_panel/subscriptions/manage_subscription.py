from presentation.manager_panel.subscriptions.create_sub import Creating_Subscription
from presentation.manager_panel.subscriptions.pay_list import Payments_List
from presentation.manager_panel.subscriptions.view_subs import Seeing_Subscription
from presentation.manager_panel import manager_menu


def manage_subscription():


    while True:
        print("-" * 8)
        print("1.Subscription Registration")
        print("2.View Payments")
        print("3.View Subscription Status")
        print("4.Return")
        choice = input("Enter Your Choice: ")
        if choice == "1":
            Creating_Subscription()
        elif choice == "2":
            Payments_List()
        elif choice == "3":
            Seeing_Subscription()
        elif choice == "4":
            manager_menu()
        else:
            print("enter number correctly")
            continue