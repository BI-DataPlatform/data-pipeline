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
    created_on: datetime = datetime.now()
    last_updated_on: datetime = datetime.now()

    def __post_init__(self):
        if self.id is None:
            self.id = uuid.uuid4().__str__()  # uuid4번 참고 https://docs.python.org/ko/3/library/uuid.html
        if self.payment is None:
            self.payment = get_payment()
            
    def to_dict(self):
        return dataclasses.asdict(self)