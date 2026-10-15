from services.users.get_users import get_users
from services.users.change_user_status import change_user_status
users = get_users(user_repository)
from datetime import datetime, timedelta
from services.subscriptions import get_subscription
subscriptions = get_subscription(subscription_repository)


def Creating_Subscription():
    while True:
        print("Creating a new Subscription\n")
        name = input("Enter the name of the user: ")
        user = None
        for u in users:
            if u['name'] == name:
                user = u
                break
        if user is None:
            print("This user does not exist!")
            return
        if user['role'] != 'member':
            print("This user is not a member!")
            return
        print("Subcriptions list: \n1 month/3 month/6 month")
        subscriptions_input = input("Enter the subscriptions you want to create:(from above) ")
        if subscriptions_input not in ['1 month', '3 month', '6 month']:
            print("Subscriptions input must be '1 month', '3 month', '6 month'")
            return
        try:
            amount = int(input("Enter the amount of subscriptions:(in Tomans)"))
            if amount <= 0:
                print("Amount must be a number greater than 0!")
                return
        except ValueError:
            print("Amount must be a number greater than 0!")
            return
        one_month_sub=datetime.now() + timedelta(days=30)
        three_month_sub = datetime.now() + timedelta(days=90)
        six_month_sub = datetime.now() + timedelta(days=180)
        if subscriptions_input == '1 month':
            end_date_val = one_month_sub
        elif subscriptions_input == '3 month':
            end_date_val = three_month_sub
        elif subscriptions_input == '6 month':
            end_date_val = six_month_sub
        else:
            end_date_val = one_month_sub
        subscription={
            'member_username': name,
            'type': subscriptions_input,
            'amount': amount,
            'payment_date': datetime.now().strftime("%Y-%m-%d"),
            'start_date': datetime.now().strftime("%Y-%m-%d"),
            'end_date': end_date_val.strftime("%Y-%m-%d")
        }
        subscriptions.append(subscription)
        print("Subscription created successfully!")
        break