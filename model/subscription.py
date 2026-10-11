class Subscription:
    def __init__(self, member, subscription_type, amount, start_date, end_date, status):
        self.member = member
        self.subscription_type = subscription_type
        self.amount = amount
        self.start_date = start_date
        self.end_date = end_date
        self.status = status
        
#subscription_type means 1 month, 3 month or 6 month plan