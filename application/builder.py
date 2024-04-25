import uuid
from faker import Faker

from domain.models import Review, ReviewTag, Reply
from application import randomizer


class ModelBuilder:

    def __init__(self):
        self.fake = Faker('ko-KR')

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
