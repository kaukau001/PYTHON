import uuid
from http import HTTPStatus
from src.exceptions.account_exceptions import CreateAccountException
from src.model.account.account import Account
from src.model.account.requests.create_account_request import CreateAccountRequest
from src.repository.account.account_repository import AccountRepository


class CreateAccountUseCase:
    def __init__(self, repository: AccountRepository()):
        self.repository = repository

    def do_action(self, account_request: CreateAccountRequest) -> Account:
        accounts = self.repository.get_account_by_cpf(account_request.national_registration)
        if len(accounts) == 0:
            account = construct_account(account_request)
            self.repository.save(account)
            return account.to_dict()
        if len(accounts) == 1:
            account = accounts[0]
            if account.get("account_number") != account_request.account_number:
                account = construct_account(account_request)
                self.repository.save(account)
                return account.to_dict()
            else:
                raise CreateAccountException('Account already exists. Please, use another account_number.',
                                             HTTPStatus.CONFLICT)
        if len(accounts) >= 2:
            raise CreateAccountException('Number of accounts exceeded for a same national registration.',
                                         HTTPStatus.BAD_REQUEST)


def construct_account(account_request: CreateAccountRequest) -> Account:
    id = uuid.uuid4()
    account = Account(
        id=id,
        account_number=account_request.account_number,
        holder_name=account_request.holder_name,
        national_registration=account_request.national_registration,
        is_pj=account_request.is_pj
    )
    return account
