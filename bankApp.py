from time import sleep

clients_list = []

class BankAccount():
    def __init__(self, name, accountNumber, balance):
        self.name = name
        self.accountNumber = accountNumber
        self.balance = balance
        clients_list.append(self)

    def add(self, amount):
        if amount > 0:
            self.balance += amount
        else:
            print("Invalid amount! Please insert a positive value.")

    def withdraw(self, amount):
        self.amount = amount
        if amount <= self.balance:
            self.balance -= amount
            print(f"\n£ {amount:.2f} withdraw from your account.\n")

        else:
            print("\nYou don't have this amount on your account.\n")


client1 = BankAccount("Willian Nomura", 10101010, 25478)
client2 = BankAccount("Pamela Alt", 20202020, 498423)
client3 = BankAccount("Scott Nomura Alt", 30303030, 58679)

print("-" * 30)
print("Bank of England".center(30))
print("-" * 30)
sleep(0.5)
print("Welcome to Bank of England app!")
sleep(0.5)
while True:
    inputAccount = int(input("Please inform your account number: "))
    foundAccount = None
    for client in clients_list:
        if client.accountNumber == inputAccount:
            foundAccount = client
            break
    if foundAccount:
        print(f"\nGood to see you {foundAccount.name}!\n")
        break
    else:
        print("Account not found!")
sleep(0.5)
while True:
        print("1 - See your balance\n"
          "2 - Add money\n"
          "3 - Withdraw money\n"
          "0 - Exit the app\n")

        sleep(1)

        option = int(input("Please choose your option: "))
        if option == 1:
            sleep(0.5)
            print(f"\nYour balance: £ {foundAccount.balance:.2f}\n")
            sleep(0.5)

        elif option == 2:
            sleep(0.5)
            amountAdd = float(input("Please inform the amount to add: "))
            foundAccount.add(amountAdd)
            print(f"\n£ {amountAdd:.2f} added to your account.\n")
            sleep(0.5)

        elif option == 3:
            sleep(0.5)
            amountWithdraw = float(input("Please inform the amount to withdraw: "))
            foundAccount.withdraw(amountWithdraw)
            sleep(0.5)

        elif option == 0:
            sleep(1)
            print("Leaving the app... Have a nice day!")
            break

        else:
            sleep(0.5)
            print("\nInvalid option.\n")
            sleep(0.5)