import dataclasses
from datetime import datetime
import uuid
from .Payment import get_payment

@dataclasses.dataclass
class FamilyAccount:
    account_id: str
    orders_left: str
    id: str = None
    payment: str = None
    created_on: datetime = None
    last_updated_on: datetime = None

    def __post_init__(self):
        if self.id is None:
            self.id = uuid.uuid4().__str__()  # uuid4번 참고 https://docs.python.org/ko/3/library/uuid.html
        if self.payment is None:
            self.payment = get_payment()
        if self.created_on is None:
            self.created_on = datetime.now()
        if self.last_updated_on is None:
            self.last_updated_on = datetime.now()
            
    def to_dict(self):
        return dataclasses.asdict(self)