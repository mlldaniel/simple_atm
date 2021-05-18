import uuid
import datetime

from manager.CardManager import CardManager


class Transaction:
    def __init__(self):  # , uuid, account_id, created_date, end_date, action='', error='', error_msg=''):
        # self.card_number = None
        self.card = None

        self.number = uuid.uuid4()
        self.created_date = datetime.datetime.now()

        self.account_id = None

        self.end_date = None
        self.action = ''

        self.error = False
        self.error_msg = ''

    def is_ok(self):
        return not self.error and not self.end_date