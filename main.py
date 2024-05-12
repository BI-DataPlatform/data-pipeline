import json

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base
from sqlalchemy.sql.expression import func

from application import service
from application import randomizer

import resources.fakeResources as res
from domain.models import *
# create an engine to connect to a database
def get_engine():
    id = 'root'
    passwd = 'root'
    host ='192.168.122.110'
    port = '30829'
    db = 'data'
    return sqlalchemy.create_engine("mysql+pymysql://" + id + ":" + passwd + "@" 
                                    + host + ":" + port + "/" + db+'?charset=utf8mb4')

engine = get_engine()

# create a session factory
Session = sessionmaker(bind=engine)

# create a base class for our model classes
Base = declarative_base()
Base.metadata.create_all(engine)

session = Session()

service = service.Service(session)


count = 50000

#카테고리, 배달회사, 배달원에 대한 상수
agencyCount = 1500 # 배달회사
dispatcherCount = 30000 # 배달원은 몇명일까..
categories = res.categories

####################################################################################
for category in categories:
        category_data = service.add_category(category)

for i in agencyCount:
    service.add_agency()

for i in dispatcherCount:
    agency_id = session.query(Agency).order_by(func.random()).first()
    service.add_dispatcher(agency_id)

####################################################################################

for i in range(0, count):
    service.add_account()
    service.add_store()
    account_id = session.query(Account).order_by(func.random()).first()
    store_id = session.query(Store).order_by(func.random()).first()
    service.add_review(account_id, store_id)
    ######################################################################################
    service.add_product(account_id)
    product_id = session.query(Product).order_by(func.random()).first()
    service.add_favorite(account_id, store_id)
    service.add_store_category(store_id)
    service.add_delivery_information(store_id)
    #####################################################################################
    service.add_family_account(account_id)
    service.add_alarm(account_id)
    service.add_cart(account_id, product_id)
    service.add_address(account_id)
    #####################################################################################

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

#배달 생성
for i in range(0, count):
    account_id = session.query(Account).order_by(func.random()).first()
    store_id = session.query(Store).order_by(func.random()).first()
    product_id = session.query(Product).order_by(func.random()).first()
    service.add_delivery()
    delivery_id = session.query(Delivery).order_by(func.random()).first()
    service.add_order(account_id, store_id, delivery_id)
    order_id = session.query(Order).order_by(func.random()).first()
    service.add_orderline(order_id, product_id)
    service.add_order_status(order_id)


#여기서 궁금점이 생기는데.. 제품은 카트에 있는걸로 해야하는 거 아닐까..
#카트에 있는걸 주문했다면 카트테이블에서 제거해야하는게 맞는데.. 전혀 그런게 없네용...
#제가 해야하는데.. 시간이 부족해서.. 이런 관계를 세팅을 못했네요..
#일단 큰 그림만 그려보았습니다.
