class Account:
    def __init__(self, name, card_number, pin, balance):
        self.__name = name
        self.__card_number = card_number
        self.__pin = pin
        self.__balance = balance



    def get_name(self):
        return self.__name

    def get_card_number(self):
        return self.__card_number

    def get_pin(self):
        return self.__pin

    def get_balance(self):
        return self.__balance


    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount

            return True
        return False
    def change_pin(self, new_pin):
        self.__pin = new_pin


