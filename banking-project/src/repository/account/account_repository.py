from src.repository.account.account_database import accounts_db
from src.model.account.account import Account
import pickle


class AccountRepository:
    def __init__(self, db_file):
        self.db_file = db_file
        try:
            with open(self.db_file, 'rb') as file:
                self.accounts_db = pickle.load(file)
        except FileNotFoundError:
            self.accounts_db = []

    def get_account_by_id(self, id: str) -> (Account, None):
        for account in accounts_db:
            if id == account.id:
                return account
        return None

    @staticmethod
    def get_account_by_cpf(national_registration: str) -> list:
        accounts = []
        for account in accounts_db:
            if national_registration == account['national_registration']:
                accounts.append(account.to_dict())
        return accounts

    def save(self, account: Account) -> None:
        self.accounts_db.append(account.to_dict())
        with open(self.db_file, 'wb') as file:
            pickle.dump(self.accounts_db, file)