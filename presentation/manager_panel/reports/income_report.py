from services.subscriptions import get_subscription
subscriptions = get_subscription(subscription_repository)

def income_report():
    while True:
        print("Total Income\n")
        total_income = sum(Sub['amount'] for Sub in subscriptions)
        print(f"Total Income : {total_income}")
        print("=" * 50)
        break
