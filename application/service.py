import pandas as pd
from pandas import DataFrame

from sqlalchemy import select, update, delete

from application.builder import ModelBuilder

from domain.models import *


class Service:

    def __init__(self, session):
        self.session = session
        self.builder = ModelBuilder()


    def add_category(self, category) -> Category:
        new_category = self.builder.random_category(category)
        self.session.add(new_category)
        return new_category

    def add_agency(self) -> Agency:
        new_agency = self.builder.random_agency()
        self.session.add(new_agency)
        return new_agency

    def add_dispatcher(self, agencyId) -> Dispatcher:
        new_dispatcher = self.builder.random_dispatcher(agencyId)
        self.session.add(new_dispatcher)
        return new_dispatcher
    
##########################################################################

    def add_account(self) -> Account:
        new_account = self.builder.random_account()
        self.session.add(new_account)
        return new_account

    def add_store(self) -> Store:
        new_store = self.builder.random_store()
        self.session.add(new_store)
        return new_store
    
    def add_review(self, accountId, storeId):
        newReview = self.builder.random_review(accountId, storeId)
        self.session.add(newReview)
        return newReview

##########################################################################

    def add_product(self, storeId) -> Product:
        new_product = self.builder.random_product(storeId)
        self.session.add(new_product)
        return new_product

    def add_favorite(self, account_id, store_id) -> Favorite:
        new_favorite = self.builder.random_favorite(account_id, store_id)
        self.session.add(new_favorite)
        return new_favorite

    def add_store_category(self, storeId) -> StoreCategory:
        new_store_category = self.builder.random_store_category(storeId)
        self.session.add(new_store_category)
        return new_store_category
    
    def add_delivery_information(self, store_id) -> DeliveryInformation:
        new_delivery_info = self.builder.random_delivery_information(store_id)
        self.session.add(new_delivery_info)
        return new_delivery_info
    
##########################################################################

    def add_family_account(self, account_id) -> FamilyAccount:
        new_family_account = self.builder.random_family_account(account_id)
        self.session.add(new_family_account)
        return new_family_account

    def add_alarm(self, account_id) -> Alarm:
        new_alarm = self.builder.random_alarm(account_id)
        self.session.add(new_alarm)
        return new_alarm

    def add_cart(self, account_id, product_id) -> Cart:
        new_cart = self.builder.random_cart(account_id, product_id)
        self.session.add(new_cart)
        return new_cart

    def add_address(self, account_id) -> Address:
        new_address = self.builder.random_address(account_id)
        self.session.add(new_address)
        return new_address

#############################################################################
    
    def add_review_tag(self, reviewId, productId):
        newReviewTag = self.builder.random_review_tag(reviewId, productId)
        self.session.add(newReviewTag)

    def add_reply(self, reviewId):
        review = self.session.execute(
            select(Review).where(Review.id == reviewId)
        ).scalar()
        newReply = self.builder.random_reply()
        self.session.add(newReply)
        setattr(review, 'reply_id', newReply.id)
        self.session.add(review)

##########################################################################

    def add_delivery(self) -> Delivery:
        new_delivery = self.random_delivery()
        self.session.add(new_delivery)
        return new_delivery

    def add_order(self, account_id, store_id, delivery_id) -> Order:
        new_order = self.random_order(account_id, store_id, delivery_id)
        self.session.add(new_order)
        return new_order

    def add_orderline(self, order_id, product_id) -> Orderline:
        new_orderline = self.random_orderline(order_id, product_id)
        self.session.add(new_orderline)
        return new_orderline

    def add_order_status(self, order_id) -> OrderStatus:
        new_order_status = self.random_order_status(order_id)
        self.session.add(new_order_status)
        return new_order_status

################################################################################


    def query_accounts_and_orders(self) -> DataFrame:
        return pd.DataFrame(self.session.execute(
            select(Account, Order).join(Order, Account.id == Order.account_id)
        ).all())

    def query_product_of_order(self, orderId) -> DataFrame:
        return pd.DataFrame(self.session.execute(
            select(Product)
            .join(Orderline, Product.id == Orderline.product_id)
            .where(Orderline.order_id == orderId)
        ).all())

    def query_all_reviews(self) -> DataFrame:
        return pd.DataFrame(self.session.execute(
            select(Review)
        ).all())
    
    def query_random_agency_id(self):
    # 대행사 테이블에서 무작위로 하나의 ID를 선택하여 반환
        random_agency = self.session.query(Agency).order_by(func.random()).first()
        if random_agency:
            return random_agency.id
        else:
            return None  # 대행사가 없는 경우 None을 반환
