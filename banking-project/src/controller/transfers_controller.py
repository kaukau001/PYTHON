from flask import Blueprint, jsonify

blueprint = Blueprint('transfers_controller', __name__)


@blueprint.route("/v1/transfer", methods=['POST'])
def create_transfer():
    return jsonify(
        {
            'message': 'not implemented yet'
        }
    )


@blueprint.route("/v1/transfer", methods=['GET'])
def get_transfer():
    return jsonify(
        {
            'message': 'not implemented yet'
        }
    )


@blueprint.route("/v1/transfer", methods=['DELETE'])
def delete_transfer():
    return jsonify(
        {
            'message': 'not implemented yet'
        }
    )

