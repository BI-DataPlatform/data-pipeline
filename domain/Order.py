import dataclasses
from datetime import datetime
import uuid

@dataclasses.dataclass
class Order:
    id: str
    account_id: str
    store_id: str
    status: str
    payment: str
    delivery_id: str
    delivery_type: str
    address: str
    phone_number: str
    price: int
    delivery_fee: int
    total_price: int
    wants_disposable: bool
    virtual_number: str
    favor_store: str
    favor_delivery: str
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