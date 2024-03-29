from datetime import datetime

class MoneyTransfer:
    def __init__(self, source, sink, amount):
        self.Source = source
        self.Sink = sink

        # Perform the transfer
        self.Source.Withdraw(amount)
        self.Sink.Deposit(amount)

        self.Amount = amount
        self.Date = datetime.now()