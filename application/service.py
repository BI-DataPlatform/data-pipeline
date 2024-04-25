import pandas as pd
from pandas import DataFrame

from sqlalchemy import select, update, delete

from application.builder import ModelBuilder

from domain.models import Account, Product, Order, Orderline, Review


class Service:

    def __init__(self, session):
        self.session = session
        self.builder = ModelBuilder()

    def add_review(self, accountId, storeId):
        newReview = self.builder.random_review(accountId, storeId)
        self.session.add(newReview)
        return newReview

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
