# from account1 import Account
# from atm import ATM
# from ui import UI
# from logic import ATMLogic
#
#
# # 1. Create ATM
# atm = ATM("Ameriabank")
#
#
# # 2. Create accounts
# user1 = Account(
#     "Anush",
#     "1111222233334444",
#     "1234",
#     1000
# )
#
# user2 = Account(
#     "Nara",
#     "5555666677778888",
#     "4321",
#     500
# )
#
#
# # 3. Add accounts to ATM
# atm.add_account(user1)
# atm.add_account(user2)
#
#
# # 4. Create UI and Logic objects
# ui = UI()
# logic = ATMLogic(atm)
#
#
#
# # 5. Login
# card, pin = ui.login_screen()
#
#
# if logic.login(card, pin):
#
#     ui.success("Login successful")
#
#     while True:
#
#         choice = ui.menu()
#
#
#         if choice == "1":
#
#             balance = logic.get_balance()
#             ui.show_balance(balance)
#
#
#         elif choice == "2":
#
#             amount = float(input("Enter amount: "))
#
#             if logic.deposit(amount):
#                 ui.success("Money deposited")
#
#
#         elif choice == "3":
#
#             amount = float(input("Enter amount: "))
#
#             if logic.withdraw(amount):
#                 ui.success("Money withdrawn")
#
#
#         elif choice == "4":
#
#             logic.logout()
#             ui.success("Goodbye")
#             break
#
#
#         else:
#             ui.error("Wrong choice")
#
#
# else:
#
#     ui.error("Wrong card or PIN")
#
