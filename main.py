# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from manager.AccountManager import AccountManager
from manager.CardManager import CardManager
from manager.TransactionManager import TransactionManager
from models.Account import Account
from models.Card import Card

account_list = []
card_list = []
transaction_list = []

account_list.append(Account("Dan", "123", "Goyang", 2000))
card_list.append(Card(1, '1234-5678-1234-5678', "123", '0000'))

account_manager = AccountManager(account_list)
card_manager = CardManager(card_list)
transaction_manager = TransactionManager(transaction_list)


def test_see_balance():
    transaction = transaction_manager.insert_card("1234-5678-1234-5678", card_manager)
    check_pin_result = transaction_manager.check_pin_number(transaction.number, "0000")
    account = transaction_manager.select_account(transaction.number, "123", account_manager)
    result = transaction_manager.see_balance(transaction.number, "123", account_manager)

    assert not transaction.error
    assert check_pin_result
    assert account
    assert result


def test_withdraw():
    transaction = transaction_manager.insert_card("1234-5678-1234-5678", card_manager)
    check_pin_result = transaction_manager.check_pin_number(transaction.number, "0000")
    account = transaction_manager.select_account(transaction.number, "123", account_manager)
    result = transaction_manager.withdraw(transaction.number, "123", account_manager, 1000)

    assert not transaction.error
    assert check_pin_result
    assert account
    assert result


def test_deposit():
    transaction = transaction_manager.insert_card("1234-5678-1234-5678", card_manager)
    check_pin_result = transaction_manager.check_pin_number(transaction.number, "0000")
    account = transaction_manager.select_account(transaction.number, "123", account_manager)
    result = transaction_manager.deposit(transaction.number, account.number, account_manager, 2000)

    assert not transaction.error
    assert check_pin_result
    assert account
    assert result


def test_error_deposit():
    transaction = transaction_manager.insert_card("1234-5678-1234-5678", card_manager)
    check_pin_result = transaction_manager.check_pin_number(transaction.number, "000")
    account = transaction_manager.select_account(transaction.number, "123", account_manager)
    result = transaction_manager.deposit(transaction.number, "123", account_manager, 2000)

    assert not transaction.error
    assert check_pin_result
    assert account
    assert result


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    test_see_balance()
    test_withdraw()
    test_deposit()

    test_error_deposit()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
