from src.repository import account
import os
ACCOUNT_REPOSITORY_MODULE_PATH = os.path.abspath(account.__file__)
ACCOUNTS_DB_PATH = ACCOUNT_REPOSITORY_MODULE_PATH.replace('__init__.py', 'accounts_db.toml')
