Define a class BankAccount with a class variable bank_name and instance variables account_holder_name, balance.
Initialize the class variables in the constructor and add methods like deposit() and withdraw() to perform transactions.
Create two instances of the BankAccount class and verify that the class variable is shared among all instances.


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
