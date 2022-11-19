#Class file

class Account:
    '''
    This class will be used to create accounts which are identified by a name and
    a balance, the balance is able to change.
    '''
    def __init__(self, name: str, balance: int =0) -> None:
        '''
        Used to identify an account.
        :param name: The name of the person who owns the account.
        :param balance: The balance of the account
        '''
        self.__name = name
        self.__balance = balance

    def deposit(self, amount: float or int) -> bool:
        '''
        Used to increase an account's balance.
        :param amount: The amount of money being added to the account's balance.
        :return: If money is added:  return True; if not: return False;
        '''
        if amount > 0:
            self.__balance += amount
            return True
        else:
            return False

    def withdraw(self, amount: float or int) -> bool:
        '''
        Used to decrease an account's balance.
        :param amount: The amount of money being subtraced from the account's balance.
        :return: If money is subtracted:  return True; if not: return False;
        '''
        if amount > 0 and amount < self.__balance:
            self.__balance -= amount
            return True
        else:
            return False

    def get_balance(self) -> float or int:
        '''
        Used to retrieve an account's balance.
        :return: an account's balance
        '''
        return self.__balance
    def get_name(self) -> str:
        '''
        Used to retrieve an account owner's name.
        :return: The account owner's name
        '''
        return self.__name
