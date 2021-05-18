import datetime

from manager.AccountManager import AccountManager
from manager.CardManager import CardManager
from models.Transaction import Transaction


class TransactionManager:
    def __init__(self, transaction_list):
        self.transaction_list = transaction_list

    def insert_card(self, card_number, card_manager: CardManager):
        try:
            transaction = Transaction()

            card = card_manager.check_card_number(card_number)
            transaction.card = card

            if not card:
                raise Exception("Card Number Not Correct")
        except Exception as ex:
            transaction.error = True
            transaction.error_msg = ex

        finally:
            self.transaction_list.append(transaction)
            return transaction

    # TODO DB 사용시 재 구현 필요(eg: django model orm 사용)
    def _get_transaction(self, transaction_number):
        for transaction in self.transaction_list:
            if transaction.number == transaction_number and transaction.is_ok():
                return transaction
        raise Exception("Wrong Transaction Number")

    def _get_transaction_by_number(self, transaction_number):
        try:
            transaction = self._get_transaction(transaction_number)
            return transaction
        except Exception as ex:
            return None

    def check_pin_number(self, transaction_number, pin_number):
        try:
            transaction = self._get_transaction_by_number(transaction_number)
            if transaction and transaction.card.pin == pin_number:
                return True
            else:
                transaction.error = True
                transaction.error_msg = "Wrong pin number"
                return False
        except:
            if transaction:
                transaction.error = True
                transaction.msg = "Wrong Transaction Number"
            return False

    def select_account(self, transaction_number, account_number, account_manager: AccountManager):
        try:
            transaction = self._get_transaction_by_number(transaction_number)
            if transaction:
                account = account_manager.get_account_by_number(account_number)
                if account.number == account_number:
                    transaction.account_id = account_number
                    return account
        except:
            return None

        return None

    def see_balance(self, transaction_number, account_number, account_manager: AccountManager):
        try:
            transaction = self._get_transaction_by_number(transaction_number)
            if transaction:
                account = account_manager.get_account_by_number(account_number)
                if account.number == account_number:
                    transaction.end_date = datetime.datetime.now()
                    transaction.action = 'see_balance'
                    return {"balance": account.balance}
        except:
            return None

        return None

    def deposit(self, transaction_number, account_number, account_manager: AccountManager, money):
        try:
            transaction = self._get_transaction_by_number(transaction_number)
            if transaction:
                account = account_manager.get_account_by_number(account_number)
                if account.number == account_number:
                    transaction.end_date = datetime.datetime.now()
                    transaction.action = 'deposit'
                    account.balance += money
                    return {"balance": account.balance, "deposit": money}
        except:
            return None

        return None

    def withdraw(self, transaction_number, account_number, account_manager: AccountManager, money):
        try:
            transaction = self._get_transaction_by_number(transaction_number)
            if transaction:
                account = account_manager.get_account_by_number(account_number)
                if account.number == account_number:
                    transaction.end_date = datetime.datetime.now()
                    transaction.action = 'deposit'
                    if account.balance > 0 and (account.balance - money) > 0:
                        account.balance -= money
                        return {"balance": account.balance, "withdraw": money}
                    else:
                        transaction.error = True
                        transaction.error_msg = "Not enought balance"
                        return {"balance": account.balance, "withdraw": 0}

        except:
            return None

        return None
