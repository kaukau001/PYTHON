from http import HTTPStatus
from marshmallow import Schema, fields, validates
from src.exceptions.account_exceptions import ValidationException
from src.utils.validators import validate_cpf, validate_cnpj


class CreateAccountRequest:
    def __init__(self, account_number, holder_name, national_registration):
        self.account_number = account_number
        self.holder_name = holder_name
        self.national_registration = national_registration
        self.is_pj = False

    @classmethod
    def from_dict(cls, data_dict):
        return cls(
            account_number=data_dict.get('account_number'),
            holder_name=data_dict.get('holder_name'),
            national_registration=data_dict.get('national_registration')
        )

    @classmethod
    def validate_params(cls, data_dict):
        if validate_cnpj(data_dict.get("national_registration")):
            data_dict["is_pj"] = True
        schema = CreateAccountRequestSchema()
        validated_data = schema.load(data_dict)
        return cls(**validated_data)


class CreateAccountRequestSchema(Schema):
    account_number = fields.Integer(required=True)
    holder_name = fields.Str(required=True, validate=fields.Length(min=1, max=900))
    national_registration = fields.Str(required=True, validate=fields.Length(min=1, max=20))
    is_pj = fields.Boolean(required=False)

    @validates("national_registration")
    def validate_cpf(self, value):
        cpf_validator = validate_cpf(value)
        cnpj_validator = validate_cnpj(value)
        if cnpj_validator:
            self.is_pj = True
        if not (cpf_validator or cnpj_validator):
            raise ValidationException("Invalid CPF/CNPJ", HTTPStatus.BAD_REQUEST)
