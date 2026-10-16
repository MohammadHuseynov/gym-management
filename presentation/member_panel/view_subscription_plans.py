from services.subscriptions.get_subscription import get_subscription

def view_subscription_plans(subscription_repository):
    plans = get_subscription(subscription_repository)
    if not plans:
        print("No subscription plans are available yet.")
        return

    print("Available subscription plans")
    print("=" * 40)
    for plan in plans:
        print(f"{plan['subscription_type']} | {plan['price']} Tomans")
