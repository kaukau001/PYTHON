from src.exceptions.account_exceptions import BusinessException
from src.model.account.account import Account
import toml
from http import HTTPStatus
from src.utils.constants import ACCOUNTS_DB_PATH


class AccountRepository:
    def __init__(self, db_file_path=ACCOUNTS_DB_PATH):
        self.accounts_db = None
        self.db_file_path = db_file_path
        try:
            with open(self.db_file_path, 'r') as file:
                self.accounts_db = toml.load(file)
        except FileNotFoundError as e:
            raise e

    def get_account_by_id(self, id: str) -> Account:
        accounts = self.accounts_db['accounts']
        filtered_accounts = filter(lambda account: account.id == id, accounts)
        if filtered_accounts:
            return filtered_accounts
        raise BusinessException("Account not found for id: {id}".replace("{id}", id), HTTPStatus.NOT_FOUND)

    def get_account_by_id_and_national_registration(self, id: str, national_registration: str) -> Account:
        accounts = self.accounts_db['accounts']
        filtered_accounts = filter(
            lambda filtered_account: filtered_account.id == id and filtered_account.national_registration == national_registration, accounts)
        account = next(filtered_accounts, None)
        if account is not None:
            return account
        raise BusinessException(f"Account not found for id: {id}"
                                f" and national registration: {national_registration}", HTTPStatus.NOT_FOUND)

    def get_account_by_cpf(self, national_registration: str) -> list:
        accounts = []
        for account_id, account in self.accounts_db.get("accounts", {}).items():
            if national_registration == account.get('national_registration'):
                accounts.append(account)
        return accounts

    def save(self, account: Account) -> None:
        num_accounts = len(self.accounts_db["accounts"]) + 1
        new_key = str(num_accounts)
        self.accounts_db["accounts"][new_key] = account.to_dict()
        with open(self.db_file_path, 'w') as file:
            toml.dump(self.accounts_db, file)
