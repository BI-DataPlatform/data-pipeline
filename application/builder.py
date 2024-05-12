import uuid
from faker import Faker
import csv
import random
from domain.models import *
from application import randomizer
import resources.fakeResources as res

class ModelBuilder:

    def __init__(self):
        self.fake = Faker('ko-KR')
        self.selected_uuids = set()

#0. 기본적으로 생성되어야할 테이블()
#################################################################

    def random_category(self, category) -> Category:
        return Category(
            id=list(res.categories.key()).index(category)+1,
            parent_category_id=None,
            name=category,
            sub_categories = ', '.join(res.categories[category]),
            created_on=datetime.now(),  # Created on
            last_updated_on=datetime.now() # Last updated on
        )

    def random_agency(self) -> Agency:
        return Agency(
            id=uuid.uuid4().hex,
            name=self.fake.company(),
            created_on=self.fake.date_time_this_decade(),
            last_updated_on=self.fake.date_time_this_decade()
        )

    def random_dispatcher(self, agencyId) -> Dispatcher:
        return Dispatcher(
            id=uuid.uuid4().hex,
            status=self.randomizer.choice(['active', 'inactive']),
            name=self.fake.name(),
            dispatcher_ride=self.randomizer.choice(['bicycle', 'motorcycle', 'car']),
            phone_number=self.fake.phone_number(),
            virtual_number=self.fake.phone_number(),
            agency_id=agencyId,
            created_on=self.fake.date_time_this_decade(),
            last_updated_on=self.fake.date_time_this_decade()
        )


#1. 가장 큰 덩이로 분류될 테이블  
######################################################################################################
    
    #어카운트쪽 수정이 필요해보이네용..
    def random_account(self) -> Account:
        return Account(
            id=uuid.uuid4().hex,
            email=self.fake.email(),
            password=self.fake.password(),
            nickname=self.fake.user_name(),
            phone_number=self.fake.phone_number(),
            virtual_number=self.fake.phone_number(),
            payment=self.fake.credit_card_number(),
            family_account_id=None,  # 이것은 생성 후에 연결할 수 있습니다.
            points=self.randomizer.randint(0, 1000),
            rank=self.randomizer.choice(['bronze', 'silver', 'gold', 'platinum']),
            role=self.randomizer.choice(['user', 'admin']),
            created_on=datetime.now(),
            last_updated_on=datetime.now()
        )

    def random_store(self) -> Store:
        return Store(
            id=uuid.uuid4().hex,
            status=self.randomizer.choice(['open', 'closed']),
            name=res.generate_company_name(),
            address=self.fake.address() + " " + self.fake.address_detail(),
            business_hours=res.generate_business_hours(),
            day_off=self.randomizer.choice(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']),
            description=self.fake.sentence(),
            min_orders=self.fake.random_int(8000, 12000, 1000),
            max_distance=self.randomizer.randint(1, 10),
            phone_number=self.fake.phone_number(),
            owner=self.fake.name(),
            taxpayer_address=self.fake.address(),
            taxpayer_id_number=self.fake.random_number(digits=10),
            ingredients=res.generate_ingredient_from(),
            created_on=datetime.now(),
            last_updated_on=datetime.now()
        )
    
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
    
#2. 덩이에 1차적으로 붙는 테이블들    
##########################################################################################################
#2-1 매장테이블
    def random_product(self, storeId) -> Product:
        return Product(
            id = uuid.uuid4().hex,
            store_id = storeId,
            name = self.fake.food.dish(),
            options = None, # 수정 필요!!!
            description = self.fake.sentence(),
            image = None,
            price = self.fake.random_int(2000, 50000, 500),
            created_on = datetime.now(),
            last_updated_on = datetime.now()
        )

    def random_favorite(self, account_id, store_id) -> Favorite:
        return Favorite(
            id=uuid.uuid4().hex,
            account_id=account_id,
            store_id=store_id,
            created_on=self.fake.date_time_this_decade(),
            last_updated_on=self.fake.date_time_this_decade()
        )
    
    def random_store_category(self, storeId) -> StoreCategory:
        category_id = random.randint(1, 13)
        return StoreCategory(
            id=uuid.uuid4().hex,
            store_id=storeId,
            category_id=category_id
        )
    
    def random_delivery_information(self, store_id) -> DeliveryInformation:
        min_fee = self.randomizer.randint(0, 5000, 500)
        max_fee = min_fee + self.randomizer.randint(0, 5000, 500)
        return DeliveryInformation(
            id=uuid.uuid4().hex,
            store_id=store_id,
            delivery_type=self.randomizer.choice(['express', 'standard']), ## 여기서 배달 타입이 뭐죠?
            min_fee = min_fee,
            max_fee = max_fee,
            created_on=datetime.now(),
            last_updated_on=datetime.now()
        )

################################################################################

#2-2 계정테이블
    def random_family_account(self, account_id) -> FamilyAccount:
        return FamilyAccount(
            id=uuid.uuid4().hex,
            account_id=account_id,
            payment=self.fake.credit_card_number(),
            orders_left=self.randomizer.randint(1, 10),
            created_on=datetime.now(),
            last_updated_on=datetime.now()
        )
    
    def random_alarm(self, account_id) -> Alarm:
        return Alarm(
            id=uuid.uuid4().hex,
            account_id=account_id,
            title=self.fake.sentence(),
            content=self.fake.text(),
            link=self.fake.url(),
            created_on=self.fake.date_time_this_decade(),
            last_updated_on=self.fake.date_time_this_decade()
        )
    
    def random_cart(self, account_id, product_id) -> Cart:
        return Cart(
            id=uuid.uuid4().hex,
            account_id=account_id,
            product_id=product_id,
            options=self.fake.text(),
            amount=self.randomizer.randint(1, 5),
            created_on=self.fake.date_time_this_decade(),
            last_updated_on=self.fake.date_time_this_decade()
        )
    
    def random_address(self, account_id) -> Address:
        return Address(
            id=uuid.uuid4().hex,
            account_id=account_id,
            is_current=self.randomizer.choice([True, False]), #하나만 트루여야하는뎅...
            name=self.fake.name(),
            first_address=self.fake.address(),
            second_address=self.fake.address_detail(),
            favor=self.fake.word(),
            created_on=self.fake.date_time_this_decade(),
            last_updated_on=self.fake.date_time_this_decade()
        )
    
##################################################################################
#2-3 리뷰테이블
    def random_reply(self) -> Reply:
        return Reply(
            id=uuid.uuid4().hex,
            content=self.fake.text(1000),
            created_on=self.fake.date_time_this_decade(),
            last_updated_on=self.fake.date_time_this_decade()
        )
    
    def random_review_tag(self, reviewId, productId) -> ReviewTag:
        return ReviewTag(
            id=uuid.uuid4().hex,
            review_id=reviewId,
            product_id=productId,
            recommend=randomizer.choose([True, False]),
            comment=self.fake.text(100)
        )
    
##################################################################################
##################################################################################
##################################################################################
#3-1 주문테이블

    def random_delivery(self) -> Delivery:
        return Delivery(
            id=uuid.uuid4().hex,
            status=self.randomizer.choice(['pending', 'processing', 'delivered']),
            delivery_type=self.randomizer.choice(['express', 'standard']),
            dispatcher_id=uuid.uuid4().hex,
            created_on=self.fake.date_time_this_decade(),
            last_updated_on=self.fake.date_time_this_decade()
        )


    def random_order(self, account_id, store_id, delivery_id) -> Order:
        return Order(
            id=uuid.uuid4().hex,
            account_id=account_id,
            store_id=store_id,
            status=self.randomizer.choice(['pending', 'processing', 'delivered']),
            payment=self.fake.credit_card_number(),
            delivery_type=self.randomizer.choice(['express', 'standard']),
            delivery_id=delivery_id,
            address=self.fake.address(),
            phone_number=self.fake.phone_number(),
            price=self.randomizer.randint(10, 200),
            delivery_fee=self.randomizer.randint(1, 10),
            total_price=self.randomizer.randint(20, 250),
            virtual_number=self.fake.phone_number(),
            wants_disposables=self.randomizer.choice([True, False]),
            favor_store=self.fake.word(),
            favor_delivery=self.fake.word(),
            created_on=self.fake.date_time_this_decade(),
            last_updated_on=self.fake.date_time_this_decade()
        )

    def random_orderline(self, order_id, product_id) -> Orderline:
        return Orderline(
            id=uuid.uuid4().hex,
            order_id=order_id,
            product_id=product_id,
            options=self.fake.text(),
            amount=self.randomizer.randint(1, 5),
            created_on=self.fake.date_time_this_decade(),
            last_updated_on=self.fake.date_time_this_decade()
        )

    def random_order_status(self, order_id) -> OrderStatus:
        return OrderStatus(
            id=uuid.uuid4().hex,
            order_id=order_id,
            progress=self.randomizer.choice(['pending', 'processing', 'shipped', 'delivered']),
            dispatcher_location=self.fake.address(),
            dispatcher_latitude=self.fake.latitude(),
            dispatcher_longtitude=self.fake.longitude(),
            created_on=self.fake.date_time_this_decade(),
            last_updated_on=self.fake.date_time_this_decade()
        )