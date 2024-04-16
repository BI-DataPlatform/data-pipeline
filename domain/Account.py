import dataclasses
from datetime import datetime
import uuid

@dataclasses.dataclass
class Account:
    email: str
    password: str
    nickname: str
    phone_number: str
    id: str = uuid.uuid4().__str__()    # uuid4번 참고 https://docs.python.org/ko/3/library/uuid.html
    virtual_number: str=""
    payment: str=""
    family_account_id: str =""
    points: int = 0
    rank: str = ""
    role: str = ""
    created_on: datetime = datetime.now()
    last_updated_on: datetime = datetime.now()
    
    
    @classmethod
    def from_dict(self, d):
        return self(**d)
    
    def to_dict(self):
        return dataclasses.asdict(self)
    
    def to_insert(self):
        return "insert into Accounts values("+ ", ".join(self.to_dict().values)+")"
                        