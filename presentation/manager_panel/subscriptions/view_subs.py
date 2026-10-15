from services.users.get_users import get_users
from services.users.change_user_status import change_user_status
users = get_users(user_repository)
from services.subscriptions import get_subscription
subscriptions = get_subscription(subscription_repository)

def Seeing_Subscription():
    while True:
        print("Seeing a User's Subscription\n")
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
        member_subs = [sub for sub in subscriptions if sub['member_username'] == name]
        if not member_subs:
            print("This user does not have a subscription!")
        else:
            latest_sub = member_subs[-1]
            print("Subscription status ; subscribed")
            print(f'Subscription type {latest_sub["type"]}')
            print(f'Subscription start date {latest_sub["start_date"]}')
            print(f'Subscription end date {latest_sub["end_date"]}')
            print("*"*50)
            break