

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
    id: str = None
    favor : str = ""
    created_on: datetime = datetime.now()
    last_updated_on: datetime = datetime.now()
        
    def to_dict(self):
        return dataclasses.asdict(self)
    
    def __post_init__(self):
        if self.id is None:
            self.id = uuid.uuid4().__str__()  # uuid4번 참고 https://docs.python.org/ko/3/library/uuid.html