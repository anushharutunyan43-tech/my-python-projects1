

class ATM:
    def __init__(self, bank_name):
        self.bank_name = bank_name
        self.accounts = []
    def add_account(self, account):
        self.accounts.append(account)
    def find_account(self, card_number):
        for account in self.accounts:
            if account.get_card_number() == card_number:
                return account
        return None
    def login(self, card_number, pin):
        account = self.find_account(card_number)
        if account and account.get_pin() == pin:
            return account
        return None

    def show_accounts(self):
        for account in self.accounts:
            print(
                account.get_name(),
                account.get_card_number(),
                account.get_balance()
            )


