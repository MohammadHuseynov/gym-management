class Subscription:
    def __init__(self, member, subscription_type, price, start_date, end_date, status):
        self.member = member
        self.subscription_type = subscription_type
        self.price = price
        self.start_date = start_date
        self.end_date = end_date
        self.status = status
