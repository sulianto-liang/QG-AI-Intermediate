# Encapsulation Example
class BankAccount:
    def __init__(self, initial_balance=0):
        self._balance = initial_balance  # Protected attribute

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            return f"Deposited ${amount}. New balance: ${self._balance}"
        return "Invalid deposit amount"

    def withdraw(self, amount):
        if 0 < amount <= self._balance:
            self._balance -= amount
            return f"Withdrew ${amount}. New balance: ${self._balance}"
        return "Insufficient funds or invalid amount"

    def get_balance(self):
        return self._balance


# Test the account
account = BankAccount(100)
print(account.deposit(50))
print(account.withdraw(30))
print(f"Current balance: ${account.get_balance()}")

# Try to access balance directly (not recommended)
print(f"Direct access: ${account._balance}")  # Works but breaks encapsulation