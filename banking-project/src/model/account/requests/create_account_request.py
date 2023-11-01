class CreateAccountRequest:
    def __init__(self,
                 account_number: str,
                 holder_name: str,
                 national_registration: str
                 ):
        self.account_number = account_number
        self.holder_name = holder_name
        self.national_registration = national_registration

    @classmethod
    def from_dict(cls, data_dict):
        return cls(
            account_number=data_dict.get('account_number', ''),
            holder_name=data_dict.get('holder_name', ''),
            national_registration=data_dict.get('national_registration', '')
        )