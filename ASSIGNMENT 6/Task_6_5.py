class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited: {amount}, New Balance: {self.balance}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew: {amount}, Remaining Balance: {self.balance}")
        else:
            print("Insufficient funds")

    def get_balance(self):
        return self.balance

# Example usage
account = BankAccount("Venu", 1000)
account.deposit(500)
account.withdraw(300)
print("Final Balance:", account.get_balance())
