from os import uname_result
import pytest
from account import Account, InsufficientFundsException
from moneytransfer import MoneyTransfer
from datetime import datetime

# Test case for creating bank accounts
def test_create_account():
    account = Account("123456", 1000)
    assert account.AccountNo == "123456"
    assert account.Balance == 1000

# Test case for depositing money into an account
def test_deposit():
    account = Account("123456", 1000)
    account.Deposit(500)
    assert account.Balance == 1500

# Test case for withdrawing money from an account with sufficient funds
def test_withdraw_sufficient_funds():
    account = Account("123456", 1000)
    account.Withdraw(500)
    assert account.Balance == 500

# Test case for withdrawing money from an account with insufficient funds
def test_withdraw_insufficient_funds():
    account = Account("123456", 100)
    with pytest.raises(InsufficientFundsException):
        account.Withdraw(500)

# Test case for transferring money from one account to another
def test_money_transfer():
    source_account = Account("source123", 1000)
    sink_account = Account("sink456", 500)
    transfer_amount = 300

    # Perform money transfer
    transfer = MoneyTransfer(source_account, sink_account, transfer_amount)

    assert transfer.Source.Balance == 700
    assert transfer.Sink.Balance == 800
    assert transfer.Amount == transfer_amount
    assert isinstance(transfer.Date, datetime)

    # Ensure exception is raised if balance is insufficient
    with pytest.raises(InsufficientFundsException):
        MoneyTransfer(source_account, sink_account, 10000)  # Attempt to transfer more than available balance

# Run tests
if uname_result == "_main_":
    pytest.main()