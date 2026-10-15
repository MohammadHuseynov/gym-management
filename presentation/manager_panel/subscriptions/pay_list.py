from services.subscriptions import get_subscription
subscriptions = get_subscription(subscription_repository)


def Payments_List():
    while True:
        print("Payments List\n")
        if not subscriptions:
            print("No Subscriptions found!")
            return
        print(f"member | subscription type | amount | payment_date")
        print("=" * 50)
        for sub in subscriptions:
            print(f"{sub['member_username']} | {sub['type']:<15} | {sub['amount']} | {sub['payment_date']}")
            print("=" * 50)
            break