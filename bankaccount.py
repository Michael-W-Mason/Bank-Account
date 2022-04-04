class BankAccount:
    all_accounts = []

    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.all_accounts.append(self)

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        self.balance -= amount
        return self

    def display_account_info(self):
        print(f"Balance: {self.balance}")

    def yield_interest(self):
        if self.balance >= 0:
            self.balance *= (1 + (self.int_rate/100))
            return self
        else:
            print("Your bank account is at a negative balance")

    @classmethod
    def print_instances(cls):
        for account in cls.all_accounts:
            print(account)


retirement = BankAccount(3, 10000)
personal = BankAccount(2, 1000)

retirement.deposit(1000).deposit(1000).deposit(1000).withdraw(
    500).yield_interest().display_account_info()
personal.deposit(1000).deposit(1000).withdraw(50).withdraw(
    400).withdraw(10).withdraw(1).yield_interest().display_account_info()

# NINJA BONUS: use a classmethod to print all instances of a Bank Account's info
BankAccount.print_instances()
