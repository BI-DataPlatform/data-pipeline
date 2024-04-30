import dataclasses
from datetime import datetime
import uuid

@dataclasses.dataclass
class Delivery:
    id: str
    status: str
    delivery_type: str
    dispatcher_id: str
    created_on: datetime = None
    last_updated_on: datetime = None

    def __post_init__(self):
        if self.id is None:
            self.id = uuid.uuid4().__str__()
        if self.dispatcher_id is None:
            self.dispatcher_id = uuid.uuid4().__str__()
        if self.created_on is None:
            self.created_on = datetime.now()
        if self.last_updated_on is None:
            self.last_updated_on = datetime.now()
            
    def to_dict(self):
        return dataclasses.asdict(self)