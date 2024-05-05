import uuid
from faker import Faker
import csv
import random
from domain.models import Review, ReviewTag, Reply
from application import randomizer


class ModelBuilder:

    def __init__(self):
        self.fake = Faker('ko-KR')
        self.selected_uuids = set()

    def randomStoreUuidPicker(self):
        with open('store_uuids.csv', newline='') as f:
            reader = csv.reader(f)
            uuids = [row[0] for row in reader if row[0] not in self.selected_uuids]  # 중복되지 않는 UUID만 선택
            if not uuids:
                return None  # 모든 UUID가 이미 선택되었을 경우
            selected_uuid = random.choice(uuids)
            self.selected_uuids.add(selected_uuid)  # 선택된 UUID를 저장
            return selected_uuid

    def random_category(self) -> Category:
        return Category()
    def random_delivery(self) -> Delivery:
        return Delivery()
    def random_store_category(self) -> Store_category:
        return Store_category()
    def random_store(self, storeId) -> Store:
        return Store()
    

    def random_review(self, accountId, storeId) -> Review:
        return Review(
            id=uuid.uuid4().hex,
            account_id=accountId,
            store_id=storeId,
            ratings_delivery=randomizer.choose([1, 2, 3, 4, 5]),
            ratings_food=randomizer.choose([1, 2, 3, 4, 5]),
            content=self.fake.text(1000),
            reply_id=None,
            is_public=True,
            shows_orders=True
        )

    def random_review_tag(self, reviewId, productId) -> ReviewTag:
        return ReviewTag(
            id=uuid.uuid4().hex,
            review_id=reviewId,
            product_id=productId,
            recommend=randomizer.choose([True, False]),
            comment=self.fake.text(100)
        )

    def random_reply(self) -> Reply:
        return Reply(
            id=uuid.uuid4().hex,
            content=self.fake.text(1000)
        )
