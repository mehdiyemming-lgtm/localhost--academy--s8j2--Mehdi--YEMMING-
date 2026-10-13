class Bank_account:
    def __init__(self, account, balance):
        self.__account_number = account
        self.__balance = balance
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited: {amount}. New balance: {self.__balance}")
        else:
            print("Deposit amount must be positive.")
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew: {amount}. New balance: {self.__balance}")
        else:
            print("Retrait impossible")
    @property
    def balance(self):
        return self.__balance

    
account = Bank_account("Alice", 1000)
print(account.balance)  # Output: 1000
account.deposit(500)  # Output: Deposited: 500. New balance: 1500
print(account.balance)
account.withdraw(300)  # Output: Withdrew: 200. New balance:
print(account.balance)
account.withdraw(5000)
print(account.balance)
