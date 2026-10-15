from presentation.member_panel.wallet.view_balance import view_balance
# from presentation.member_panel.wallet.deposit_wallet import deposit_wallet
from presentation.member_panel.wallet.view_transactions import view_transaction
from presentation.member_panel.wallet.pay_renew_subscription import pay_renew_subscription



def manage_wallet():
    print("-" * 8)
    print("1.View Balance")
    print("2.Deposit Wallet")
    print("3.View Transactions")
    print("4.Pay Or Renew Subscription")
    print("5.Exit")

    try:
        user_choice = int(input("enter a number choice: "))
    except:
        raise ValueError("please enter a number: ")

    if user_choice == 1:
        view_balance()

    elif user_choice == 2:
        #deposit_wallet()
        pass
    
    elif user_choice == 3:
        view_transaction()

    elif user_choice == 4:
        pay_renew_subscription()

    elif user_choice == 5:
        pass