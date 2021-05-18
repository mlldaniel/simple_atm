class AccountManager:
    def __init__(self, acount_list):
        self.account_list = acount_list

    def get_account_by_number(self, account_number):
        for account in self.account_list:
            if account.number == account_number:
                return account

        return None