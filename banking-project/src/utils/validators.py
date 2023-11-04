from validate_docbr import CNPJ, CPF


def validate_cnpj(value: str):
    cnpj_validator = CNPJ()
    return cnpj_validator.validate(value)


def validate_cpf(value: str):
    cpf_validator = CPF()
    return cpf_validator.validate(value)
