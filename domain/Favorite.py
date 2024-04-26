import dataclasses
from datetime import datetime
import uuid


@dataclasses.dataclass
class Favorite:
    account_id: str
    store_id : str
    id: str = None
    created_on: datetime = None
    last_updated_on: datetime = None
        
    def to_dict(self):
        return dataclasses.asdict(self)
    
    def __post_init__(self):
        if self.id is None:
            self.id = uuid.uuid4().__str__()  # uuid4번 참고 https://docs.python.org/ko/3/library/uuid.html
        if self.created_on is None:
            self.created_on = datetime.now()
        if self.last_updated_on is None:
            self.last_updated_on = datetime.now()