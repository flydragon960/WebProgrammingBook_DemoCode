# oop_02_encapsulation.py
# Demonstrates: Private attributes, name mangling, controlled access via methods

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner          # public attribute
        self._bank = "PyBank"       # _single underscore: internal use by convention
        self.__balance = balance    # __double underscore: name-mangled (private)

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited ${amount}. New balance: ${self.__balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.__balance}")
        else:
            print("Invalid or insufficient funds.")

    def get_balance(self):
        return self.__balance       # controlled read access


account = BankAccount("Alice", 1000)
account.deposit(500)                # Deposited $500. New balance: $1500
account.withdraw(200)               # Withdrew $200. New balance: $1300
print(account.get_balance())        # 1300
print(account.owner)                # Alice   (public, accessible directly)
print(account._bank)                # PyBank  (accessible but signals: don't touch)

# Attempting to access the private attribute directly
try:
    print(account.__balance)        # AttributeError
except AttributeError as e:
    print(f"Error: {e}")

# Name mangling: Python renames __balance to _BankAccount__balance
print(account._BankAccount__balance)   # 1300 (accessible via mangled name, but avoid this)
