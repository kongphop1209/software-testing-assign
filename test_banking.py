import banking

class TestBankAccount:
    def test_deposit(self):
        obj = banking.BankAccount(10001, 5000)
        obj.deposit(100)
        obj.deposit(500)
        obj.deposit(400)
        assert obj.balance == 6000
        
    def test_withdraw(self):
        obj = banking.BankAccount(10002, 1000)
        obj.withdraw(100)
        obj.withdraw(200)
        obj.withdraw(400)
        assert obj.balance == 300
        
        