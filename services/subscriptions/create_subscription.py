from model.subscription import Subscription


def create_subscription(subscription_type, price, subscription_repository):
    subscription_type = subscription_type.strip().lower()
    valid_types = ("1 month", "3 month", "6 month")
    if subscription_type not in valid_types:
        raise ValueError("Subscription type must be '1 month', '3 month', or '6 month'.")

    try:
        price = int(price)
    except (ValueError, TypeError):
        raise ValueError("price must be a number.")

    if price <= 0:
        raise ValueError("price must be greater than zero.")

    if any(plan["subscription_type"] == subscription_type for plan in subscription_repository.get_all()):
        raise ValueError("This subscription plan already exists.")

    subscription = Subscription(subscription_type, price)
    subscription_repository.add(subscription)
    return True
