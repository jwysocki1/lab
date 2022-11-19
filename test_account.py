from account import *
#Class testing file

class Test:
    def setup_method(self):
        self.account1 = Account(Nathan)
        self.account2 = Account(Bronny, 100)
        self.account3 = Account(Jasmine, 500.75)

    def teardown_method(self):
        del self.account1
        del self.account2
        del self.account3

    def test_init(self):
        assert self.account1.get_name() == "Nathan"
        assert self.account1.get_balance() == 0
        assert self.account2.get_name() == "Bronny"
        assert self.account2.get_balance() == 100
        assert self.account3.get_name() == "Jasmine"
        assert  self.account3.get_balance() == 500.75

    def test_deposit(self):
        assert self.account2.deposit(25.50) == True
        assert self.account1.deposit(0) == False
        assert self.account3.deposit(-200) == False

    def test_withdraw(self):
        assert self.account1.withdraw(-900.34) == False
        assert self.account2.withdraw(50) == True
        assert self.account3.withdraw(0) == False