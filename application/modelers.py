import uuid

from domain.models import Account, FamilyAccount, Address, Alarm, Store, Favorite, Product, Cart, DeliveryInformation, \
    Review, ReviewTag, Reply
from application import randomizer


def random_account() -> Account:
    return Account(
        id=uuid.uuid4().hex,
        email=randomizer.email(),
        password=uuid.uuid4(),
        nickname=randomizer.name_korean(randomizer.random_binary(0.5)),
        phone_number="010-" + randomizer.numbers(4) + "-" + randomizer.numbers(4),
        virtual_number="05" + randomizer.numbers(2) + "-" + randomizer.numbers(4) + "-" + randomizer.numbers(4),
        payment=randomizer.choose(["카카오페이", "네이버페이", "신용카드"]),
        family_account_id=None,
        points=0,
        rank="일반",
        role="USER"
    )

def random_family_account(owner_id) -> FamilyAccount:
    return FamilyAccount(
        id=uuid.uuid4().hex,
        account_id=owner_id,
        payment=randomizer.choose(["카카오페이", "네이버페이", "신용카드"]),
        orders_left=randomizer.choose([10, 20, 30])
    )

def random_address(user_id) -> Address:
    return Address(
        id=uuid.uuid4().hex,
        is_current=True,
        account_id=user_id,
        name="기본주소",
        first_address="서울시",
        second_address="99호",
        favor=randomizer.choose(["조심히 배달해주세요", "문 앞에 놓아주세요", "부재 시 연락 주세요"])
    )


def random_alarm(user_id) -> Alarm:
    return Alarm(
        id=uuid.uuid4().hex,
        account_id=user_id,
        title="알림 제목",
        content="알림 내용",
        link="알림 링크",
    )

def random_store() -> Store:
    return Store(
        id=uuid.uuid4().hex,
        status="영업중",
        name="일반음식점",
        address="서울시 어딘가",
        business_hours="오후 1시 ~ 오후 9시",
        day_off="4/1,4/15",
        description="안녕하세요 맛있는 식당 입니다",
        min_orders=15000,
        phone_number="010-" + randomizer.numbers(4) + "-" + randomizer.numbers(4),
        owner=randomizer.name_korean(randomizer.random_binary(0.5)),
        taxpayer_address="서울시 어딘가",
        taxpayer_id_number="00-000-00000",
        ingredients="돼지고기(국산),김치(중국산)"
    )

def random_delivery_info(storeId, type) -> DeliveryInformation:
    return DeliveryInformation(
        id=uuid.uuid4().hex,
        store_id=storeId,
        delivery_type=type,
        min_fee=2000,
        max_fee=4000
    )

def favorite(account_id, store_id) -> Favorite:
    return Favorite(
        id=uuid.uuid4().hex,
        account_id=account_id,
        store_id=store_id
    )

def random_product(storeId) -> Product:
    return Product(
        id=uuid.uuid4().hex,
        store_id=storeId,
        name='음식',
        options='{}',
        description='음식 소개',
        image='',
        price=randomizer.choose(list(range(5, 21))) * 1000
    )

def cart(accountId, productId) -> Cart:
    return Cart(
        id=uuid.uuid4().hex,
        account_id=accountId,
        product_id=productId,
        options='{}',
        amount=randomizer.choose(list(range(1, 5)))
    )

def random_review(accountId, storeId) -> Review:
    return Review(
        id=uuid.uuid4().hex,
        account_id=accountId,
        store_id=storeId,
        ratings_delivery=randomizer.choose([1, 2, 3, 4, 5]),
        ratings_food=randomizer.choose([1, 2, 3, 4, 5]),
        content="좋아요",
        reply_id=None,
        is_public=True,
        shows_orders=True
    )

def random_review_tag(reviewId, productId) -> ReviewTag:
    return ReviewTag(
        id=uuid.uuid4().hex,
        review_id=reviewId,
        product_id=productId,
        recommend=randomizer.choose([True, False]),
        comment="맛있어요"
    )

def random_reply() -> Reply:
    return Reply(
        id=uuid.uuid4().hex,
        content="감사합니다"
    )