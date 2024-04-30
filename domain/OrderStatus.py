import dataclasses
from datetime import datetime
import uuid

@dataclasses.dataclass
class OrderStatus:
    id: str
    order_id: str
    progress: str
    dispatcher_location: str
    dispatcher_latitude: str
    dispatcher_longitude: str
    created_on: datetime = None
    last_updated_on: datetime = None

    def __post_init__(self):
        if self.id is None:
            self.id = uuid.uuid4().__str__()
        if self.created_on is None:
            self.created_on = datetime.now()
        if self.last_updated_on is None:
            self.last_updated_on = datetime.now()
            
    def to_dict(self):
        return dataclasses.asdict(self)