class BankAccount:
    def __init__(self, account_holder_name, balance):
        self.account_holder_name = account_holder_name
        self.balance = balance
        bank_name = "BankOfAmerica"

    def deposit(self):
        print("this is a deposit.")

    def withdraw(self):
        print("This is a withdraw.")


pedro = BankAccount("pedro", 0)
marta = BankAccount("marta", 100)

print(pedro.bank_name)
print(marta.bank_name)
