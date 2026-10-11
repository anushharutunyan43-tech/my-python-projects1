class Transaction:
    def __init__(self, account):
        self.account = account




class Deposit(Transaction):
    def __init__(self, account, amount):
        super().__init__(account)
        self.amount = amount

    def execute(self):
        self.account.deposit(self.amount)
        print("Deposit Successful")


class Withdraw(Transaction):
    def __init__(self, account, amount):
        super().__init__(account)
        self.amount = amount
    def execute(self):
        if self.account.Withdraw(self.amount):
            print("Withdrawal successful")
        else:
            print("NOt enough balance")