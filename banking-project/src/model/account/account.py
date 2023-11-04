from uuid import UUID


class Account:
    def __init__(self,
                 id: UUID,
                 account_number: str,
                 holder_name: str,
                 national_registration: str,
                 is_pj: bool
                 ):
        self.id = id
        self.account_number = account_number
        self.holder_name = holder_name
        self.national_registration = national_registration
        self.balance = 0
        self.is_pj = is_pj

    def to_dict(self):
        account_dict = {
            "id": str(self.id),
            "account_number": self.account_number,
            "holder_name": self.holder_name,
            "national_registration": self.national_registration,
            "balance": self.balance,
            "is_pj": self.is_pj
        }
        return account_dict
