import uuid

from src.exceptions.account_exceptions import CreateAccountException
from src.model.account.account import Account
from src.model.account.requests.create_account_request import CreateAccountRequest
from src.repository.account.account_repository import AccountRepository
from flask import jsonify


class CreateAccountUseCase:
    def __init__(self):
        self.repository = AccountRepository()

    def doAction(self, account_request: CreateAccountRequest) -> Account:
        try:
            accounts = self.repository.get_account_by_cpf(account_request.national_registration)
            if len(accounts) == 0:
                account = construct_account(account_request)
                self.repository.save(account)
                return account
            if len(accounts) == 1:
                for account in accounts:
                    if account.account_number != account_request.account_number:
                        account = construct_account(account_request)
                        self.repository.save(account)
                        return account
            if len(accounts) > 2:
                raise CreateAccountException(
                    jsonify({
                        'message': 'Number of accounts exceeded for a same national registration'
                    }))
        except CreateAccountException as e:
            raise e.message


def construct_account(account_request: CreateAccountRequest) -> Account:
    id = uuid.uuid4()
    account = Account(
        id=id,
        account_number=account_request.account_number,
        holder_name=account_request.holder_name,
        national_registration=account_request.national_registration
    )
    return account
