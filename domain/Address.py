

import dataclasses
from datetime import datetime
import uuid


@dataclasses.dataclass
class Address:
    account_id: str
    is_current: bool
    name: str
    first_address: str
    second_address: str
    favor : str = ""
    id: str  = uuid.uuid4().__str__()    # uuid4번 참고 https://docs.python.org/ko/3/library/uuid.html
    created_on: datetime = datetime.now()
    last_updated_on: datetime = datetime.now()