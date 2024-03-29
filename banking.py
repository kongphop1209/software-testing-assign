class BankAccount:
    def __init__(self, id, balance):
        self.id = id
        self.balance = balance
        
    def deposit(self, sum):
        self.balance += sum
        
    def withdraw(self, sum):
        self.balance -= sum