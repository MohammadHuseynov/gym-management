class Wallet:
    def __init__(self, member, balance=0):
        self.member = member
        self.balance = balance


    #@property is a Getter: this def would be executed when you write: print(battery.balance)
    @property
    def balance(self):
        return self._balance

    #balance.setter is a Setter: this function would be called when you run: battery.voltage = 12
    @balance.setter
    def balance(self, value):
        if not isinstance(value, (int, float)):
            raise ValueError("Balance must be a number")

        if value < 0:
            raise ValueError("Balance cannot be negative")

        self._balance = value



class Transaction:
    def __init__(self, transaction_type, amount, date, description, tracking_number):
        self.transaction_type = transaction_type
        self.amount = amount
        self.date = date
        self.description = description
        self.tracking_number = tracking_number