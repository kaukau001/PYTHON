
from flask import Flask
from flask_request_id_header.middleware import RequestID
from src.controller import (account_controller, transfers_controller)


application = Flask(__name__)
application.config['REQUEST_ID_UNIQUE_VALUE_PREFIX'] = 'FOO-'
application.config['JSON_SORT_KEYS'] = False
application.register_blueprint(account_controller.blueprint)
application.register_blueprint(transfers_controller.blueprint)
RequestID(application)

if __name__ == '__main__':
    application.run(debug=False)
