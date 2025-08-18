from abc import ABC, abstractmethod

class Bankaccount(ABC):
    @abstractmethod
    def deposit(self, amount):
        pass

    @abstractmethod
    def withdraw(self, amount):
        pass

    @abstractmethod
    def get_balance(self):
        pass


class Savingaccount(Bankaccount):
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. New Balance: {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance")
        else:
            self.balance -= amount
            print(f"Withdrew {amount}. New Balance: {self.balance}")

    def get_balance(self):
        print(f"Balance: {self.balance}")


class Currentaccount(Bankaccount):
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. New Balance: {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance")
        else:
            self.balance -= amount
            print(f"Withdrew {amount}. New Balance: {self.balance}")

    def get_balance(self):
        print(f"Balance: {self.balance}")


# Demo
accounts = [Currentaccount(1000), Savingaccount(2000)]

for acc in accounts:
    acc.withdraw(300)
    acc.deposit(600)
    acc.get_balance()
