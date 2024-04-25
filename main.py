import json

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base

from application import service
from application import randomizer

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
