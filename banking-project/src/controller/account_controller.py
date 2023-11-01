from flask import Blueprint, jsonify, request

from src.model.account.requests.create_account_request import CreateAccountRequest
from src.use_cases.accounts_use_cases.create_account_use_case import CreateAccountUseCase
from src.repository.account.account_repository import AccountRepositoy

blueprint = Blueprint('account_controller', __name__)

account_repository = AccountRepositoy()


@blueprint.route("/")
def index() -> str:
    return "Bye World"


@blueprint.route("/v1/account", methods=['POST'])
def create_account():
    create_account_request = CreateAccountRequest.from_dict(request.get_json())
    response = CreateAccountUseCase().doAction(create_account_request)
    return jsonify(response.to_dict())


@blueprint.route("/v1/account", methods=['GET'])
def get_account():
    return jsonify(
        {
            'message': 'not implemented yet'
        }
    )


@blueprint.route("/v1/account", methods=['DELETE'])
def delete_account():
    return jsonify(
        {
            'message': 'not implemented yet'
        }
    )


@blueprint.route("/v1/account", methods=['UPDATE'])
def update_account():
    return jsonify(
        {
            'message': 'not implemented yet'
        }
    )
