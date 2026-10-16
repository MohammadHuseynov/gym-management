from model.subscription import Subscription

class User:
    def __init__(self, name, username, password, email, role, is_active=True):
        self.name = name
        self.username = username
        self.password = password
        self.email = email
        self.role = role
        self.is_active = is_active

class Manager(User):
    pass


class Trainer(User):
    pass



class Member(User):
    def __init__(self, name, username, password, email, role, user_balance, user_subscription, is_active=True):
        super().__init__(name, username, password, email, role, is_active)
        self.user_balance = user_balance
        self.user_subscription = user_subscription
        