import uuid
from http import HTTPStatus

from flask import Blueprint, jsonify, request

from src.exceptions.account_exceptions import CreateAccountException, ValidationException
from src.model.account.requests.create_account_request import CreateAccountRequest, CreateAccountRequestSchema
from src.use_cases.accounts_use_cases.create_account_use_case import CreateAccountUseCase
from src.repository.account.account_repository import AccountRepository


blueprint = Blueprint('account_controller', __name__)

account_repository = AccountRepository()


@blueprint.route("/")
def index() -> str:
    return "Bye World"


@blueprint.route("/v1/account", methods=['POST'])
def create_account():
    request_id = uuid.uuid4()
    try:
        create_account_request = CreateAccountRequest.validate_params(request.get_json())
        response = CreateAccountUseCase(account_repository).do_action(create_account_request)
        return jsonify(response), HTTPStatus.OK
    except CreateAccountException as e:
        return jsonify({'message': e.message, "uuid": request_id}), e.status_code
    except ValidationException as e:
        return jsonify({'message': e.message, "uuid": request_id}), e.status_code




@blueprint.route("/v1/account", methods=['GET'])
def get_account():
    request_id = uuid.uuid4()
    return jsonify(
        {
            'message': 'not implemented yet'
        }
    )


@blueprint.route("/v1/account", methods=['DELETE'])
def delete_account():
    request_id = uuid.uuid4()
    return jsonify(
        {
            'message': 'not implemented yet'
        }
    )


@blueprint.route("/v1/account", methods=['UPDATE'])
def update_account():
    request_id = uuid.uuid4()
    return jsonify(
        {
            'message': 'not implemented yet'
        }
    )
