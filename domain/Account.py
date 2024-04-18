import dataclasses
from datetime import datetime
import uuid
from .Payment import get_payment


@dataclasses.dataclass
class Account:
    email: str 
    password: str
    nickname: str 
    phone_number: str 
    id: str = None
    virtual_number: str=""
    payment: str = get_payment()
    family_account_id: str =""   # nullable
    points: int = 0
    rank: str = ""
    role: str = ""
    created_on: datetime = datetime.now()
    last_updated_on: datetime = datetime.now()
    
    def __post_init__(self):
        if self.id is None:
            self.id = uuid.uuid4().__str__()  # uuid4번 참고 https://docs.python.org/ko/3/library/uuid.html
            
    @classmethod
    def from_dict(self, d):
        return self(**d)
    
    def to_dict(self):
        return dataclasses.asdict(self)
    
    def to_insert(self):
        return "insert into Accounts values("+ ", ".join(self.to_dict().values)+")"
                        