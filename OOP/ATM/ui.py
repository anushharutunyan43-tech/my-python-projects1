class UI:

    def login_screen(self):
        print("\n===== ATM LOGIN =====")

        card = input("Enter card number: ")
        pin = input("Enter PIN: ")

        return card, pin


    def menu(self):
        print("\n===== MENU =====")
        print("1. Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

        return input("Choose: ")


    def show_balance(self, balance):
        print(f"\nYour balance is: {balance}")


    def success(self, message):
        print(f"\n {message}")


    def error(self, message):
        print(f"\n {message}")