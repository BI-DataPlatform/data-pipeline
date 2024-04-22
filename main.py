import json
import uuid

from sqlalchemy import create_engine, select
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base

from application import service
from application import randomizer

from domain.models import Account, Address, Store, Order, Orderline

# create an engine to connect to a database
with open('conf.json') as f:
    config = json.load(f)
engine = create_engine(config['url'])

# create a session factory
Session = sessionmaker(bind=engine)

# create a base class for our model classes
Base = declarative_base()
Base.metadata.create_all(engine)

session = Session()

service = service.Service(session)

# 새로 가입한 사용자
for i in range(100):
    service.account_register()
session.commit()

# 알림
accountIds = service.query_all_accounts().map(lambda x: x.id)
for accountId in accountIds.values.tolist():
    randomizer.random_call(
        service.send_alarm,
        args=[accountId],
        probability=0.1
    )
session.commit()

# 가족 계정 생성
for i in range(5):
    sole_account_ids = service.query_sole_accounts().map(lambda x: x.id)
    family = randomizer.sample(sole_account_ids.values.tolist(), 4)
    service.family_account_register(family)
session.commit()

# 매장 생성
for i in range(10):
    service.add_store()
session.commit()

# 배달 정보 생성
storeIds = service.query_all_stores().map(lambda x: x.id)
for storeId in storeIds.values.tolist():
    service.add_delivery_information(storeId, '한집배달')
    service.add_delivery_information(storeId, '알뜰배달')

# 매장 찜
account_ids = service.query_all_accounts().map(lambda x: x.id)
store_ids = service.query_all_stores().map(lambda x: x.id)
for account_id in account_ids.values.tolist():
    for store_id in store_ids.values.tolist():
        randomizer.random_call(
            service.add_favorite,
            args=[account_id, store_id],
            probability=0.01
        )
session.commit()

# 음식 생성
storeIds = service.query_all_stores().map(lambda x: x.id)
for storeId in storeIds.values.tolist():
    for i in range(10):
        service.add_product(storeId)
session.commit()

# 장바구니 담기
accountIds = service.query_all_accounts().map(lambda x: x.id)
storeIds = service.query_all_stores().map(lambda x: x.id)
for accountId in accountIds.values.tolist():
    service.clear_cart(accountId)
    storeId = randomizer.choose(storeIds.values.tolist())
    productIds = service.query_products(storeId).map(lambda x: x.id)
    for productId in productIds.values.tolist():
        randomizer.random_call(
            service.add_cart,
            args=[accountId, productId],
            probability=0.1
        )
session.commit()

# 주문 생성
accounts = service.query_accounts_in_cart()
for account in accounts.values.tolist():
    address = service.query_current_address(account.id)
    store = service.query_one_store_in_cart(account.id)
    delivery_infos = service.query_delivery_info_of_store(store.id).values.tolist()
    delivery_info = randomizer.choose(delivery_infos)[0]
    cart = service.query_products_in_cart(account.id)
    orderId = uuid.uuid4().hex
    orderlines = []
    price = 0
    for idx, row in cart.iterrows():
        orderline = Orderline(
            id=uuid.uuid4().hex,
            order_id=orderId,
            product_id=row['Product'].id,
            options=row['options'],
            amount=row['amount']
        )
        orderlines.append(orderline)
        price += row['Product'].price * row['amount']
    order = Order(
        id=orderId,
        account_id=account.id,
        store_id=storeId,
        status='CREATED',
        payment=account.payment,
        delivery_type=delivery_info.delivery_type,
        address=address.first_address+' '+address.second_address,
        phone_number=account.phone_number,
        price=price,
        delivery_fee=delivery_info.max_fee,
        total_price=price + delivery_info.max_fee,
        virtual_number=account.virtual_number,
        wants_disposables=True,
        favor_store='가게요청',
        favor_delivery=address.favor
    )
    for orderline in orderlines:
        session.add(orderline)
    session.add(order)

# 리뷰, 리뷰 태그 생성
accountOrders = service.query_accounts_and_orders()
accounts = accountOrders['Account']
orders = accountOrders['Order']
for i in range(accounts.size):
    newReview = service.add_review(accounts[i].id, orders[i].store_id)
    reviewItems = service.query_product_of_order(orders[i].id)
    for idx, row in reviewItems.iterrows():
        service.add_review_tag(newReview.id, row['Product'].id)

# 사장님 답글 생성
reviews = service.query_all_reviews()
for idx, row in reviews.iterrows():
    randomizer.random_call(service.add_reply, args=[row['Review'].id], probability=0.3)
session.commit()
