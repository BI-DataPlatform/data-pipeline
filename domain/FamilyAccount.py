import dataclasses
from datetime import datetime
import uuid
from .Payment import get_payment

@dataclasses.dataclass
class FamilyAccount:
    account_id: str
    orders_left: str
    payment: str = get_payment()
    id: str = uuid.uuid4().__str__()    # uuid4번 참고 https://docs.python.org/ko/3/library/uuid.html
    created_on: datetime = datetime.now()
    last_updated_on: datetime = datetime.now()

