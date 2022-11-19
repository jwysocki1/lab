

class Account:
    def __init__(self, name, balance=0):
        self.__name = name
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            return True
        else:
            return False

    def withdraw(self, amount):
        if amount > 0 and amount < self.__balance:
            self.__balance -= amount
            return True
        else:
            return False

    def get_balance(self):
        return self.__balance
    def get_name(self):
        return self.__name
