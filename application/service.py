import pandas as pd
from pandas import DataFrame

from sqlalchemy import select, update, delete

from application import modelers

from domain.models import Account, Address, Store, Cart, Product, DeliveryInformation, Order, Orderline, Review, Reply


class Service:

    def __init__(self, session):
        self.session = session

    def account_register(self):
        new_account = modelers.random_account()
        self.session.add(new_account)
        new_address = modelers.random_address(new_account.id)
        self.session.add(new_address)

    def send_alarm(self, account_id):
        new_alarm = modelers.random_alarm(account_id)
        self.session.add(new_alarm)

    def family_account_register(self, account_ids):
        new_family_account = modelers.random_family_account(account_ids[0])
        self.session.add(new_family_account)
        self.session.execute(
            update(Account).where(Account.id.in_(account_ids)).values(family_account_id=new_family_account.id)
        )

    def add_store(self):
        new_store = modelers.random_store()
        self.session.add(new_store)

    def add_delivery_information(self, storeId, type):
        new_delivery_info = modelers.random_delivery_info(storeId, type)
        self.session.add(new_delivery_info)

    def add_favorite(self, account_id, store_id):
        new_favorite = modelers.favorite(account_id, store_id)
        self.session.add(new_favorite)

    def add_product(self, storeId):
        newProduct = modelers.random_product(storeId)
        self.session.add(newProduct)

    def add_cart(self, accountId, productId):
        newCart = modelers.cart(accountId, productId)
        self.session.add(newCart)

    def add_review(self, accountId, storeId):
        newReview = modelers.random_review(accountId, storeId)
        self.session.add(newReview)
        return newReview

    def add_review_tag(self, reviewId, productId):
        newReviewTag = modelers.random_review_tag(reviewId, productId)
        self.session.add(newReviewTag)

    def add_reply(self, reviewId):
        review = self.session.execute(
            select(Review).where(Review.id == reviewId)
        ).scalar()
        newReply = modelers.random_reply()
        self.session.add(newReply)
        setattr(review, 'reply_id', newReply.id)
        self.session.add(review)

    def clear_cart(self, accountId):
        self.session.execute(
            delete(Cart).where(Cart.account_id == accountId)
        )

    def query_all_accounts(self) -> DataFrame:
        return pd.DataFrame(self.session.execute(
            select(Account)
        ).all())

    def query_sole_accounts(self) -> DataFrame:
        return pd.DataFrame(self.session.execute(
            select(Account).where(Account.family_account_id == None)
        ).all())

    def query_current_address(self, accountId) -> Address:
        return self.session.execute(
            select(Address).where(Address.account_id == accountId, Address.is_current).limit(1)
            ).scalar()

    def query_accounts_in_cart(self) -> DataFrame:
        return pd.DataFrame(self.session.execute(
            (select(Cart.account_id, Account).distinct()).join(Account, Cart.account_id == Account.id)
        ).all())['Account']

    def query_products_in_cart(self, accountId) -> DataFrame:
        return pd.DataFrame(self.session.execute(
            (select(Product, Cart.options, Cart.amount).join(Cart, Product.id == Cart.product_id)
             .join(Account, Cart.account_id == Account.id)
             .where(Account.id == accountId))
        ).all())

    def query_all_stores(self) -> DataFrame:
        return pd.DataFrame(self.session.execute(
            select(Store)
        ).all())

    def query_products(self, storeId) -> DataFrame:
        return pd.DataFrame(self.session.execute(
            select(Product).where(Product.store_id == storeId)
        ).all())

    def query_one_store_in_cart(self, accountId) -> Store:
        return self.session.execute(
            select(Store)
            .where(Store.id.in_(
                select(Product.store_id).distinct()
                .join(Cart, Cart.product_id == Product.id)
                .where(Cart.account_id == accountId)
            )).limit(1)).scalar()

    def query_delivery_info_of_store(self, storeId) -> DataFrame:
        return pd.DataFrame(self.session.execute(
            select(DeliveryInformation).where(DeliveryInformation.store_id == storeId)
        ).all())

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
