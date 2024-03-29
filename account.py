class InsufficientFundsException(Exception):
    pass

class Account:
    def __init__(self, accountNo, balance):
        self.AccountNo = accountNo
        self.Balance = balance

    def Deposit(self, amount):
        self.Balance += amount

    def Withdraw(self, amount):
        if self.Balance < amount:
            raise InsufficientFundsException("Insufficient funds in the account.")
        self.Balance -= amount