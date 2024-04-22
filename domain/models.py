import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()


class Account(Base):

    __tablename__ = 'accounts'

    id = sa.Column(sa.String(64), primary_key=True, nullable=False)
    email = sa.Column(sa.String(50))
    password = sa.Column(sa.String(64))
    nickname = sa.Column(sa.String(20))
    phone_number = sa.Column(sa.String(16))
    virtual_number = sa.Column(sa.String(16))
    payment = sa.Column(sa.String(64))
    family_account_id = sa.Column(sa.ForeignKey('family_accounts.id'), nullable=True)
    points = sa.Column(sa.Integer())
    rank = sa.Column(sa.String(8))
    role = sa.Column(sa.String(8))
    created_on = sa.Column(sa.TIMESTAMP(), default=datetime.utcnow)
    last_updated_on = sa.Column(sa.TIMESTAMP(), default=datetime.utcnow)


class FamilyAccount(Base):

    __tablename__ = 'family_accounts'

    id = sa.Column(sa.String(64), primary_key=True, nullable=False)
    account_id = sa.Column(sa.ForeignKey('accounts.id'), nullable=False)
    payment = sa.Column(sa.String(64))
    orders_left = sa.Column(sa.Integer())
    created_on = sa.Column(sa.TIMESTAMP(), default=datetime.utcnow)
    last_updated_on = sa.Column(sa.TIMESTAMP(), default=datetime.utcnow)


class Address(Base):

    __tablename__ = 'addresses'

    id = sa.Column(sa.String(64), primary_key=True, nullable=False)
    account_id = sa.Column(sa.ForeignKey('accounts.id'), nullable=False)
    is_current = sa.Column(sa.Boolean())
    name = sa.Column(sa.String(20))
    first_address = sa.Column(sa.String(100))
    second_address = sa.Column(sa.String(100))
    favor = sa.Column(sa.String(100))
    created_on = sa.Column(sa.TIMESTAMP(), default=datetime.utcnow)
    last_updated_on = sa.Column(sa.TIMESTAMP(), default=datetime.utcnow)


class Favorite(Base):

    __tablename__ = 'favorites'

    id = sa.Column(sa.String(64), primary_key=True, nullable=False)
    account_id = sa.Column(sa.ForeignKey('accounts.id'), nullable=False)
    store_id = sa.Column(sa.ForeignKey('stores.id'), nullable=False)
    created_on = sa.Column(sa.TIMESTAMP(), default=datetime.utcnow)
    last_updated_on = sa.Column(sa.TIMESTAMP(), default=datetime.utcnow)


class Store(Base):

    __tablename__ = 'stores'

    id = sa.Column(sa.String(64), primary_key=True, nullable=False)
    status = sa.Column(sa.String(10))
    name = sa.Column(sa.String(100))
    address = sa.Column(sa.String(200))
    business_hours = sa.Column(sa.String(100))
    day_off = sa.Column(sa.String(100))
    description = sa.Column(sa.Text())
    min_orders = sa.Column(sa.Integer())
    max_distance = sa.Column(sa.Integer())
    phone_number = sa.Column(sa.String(16))
    owner = sa.Column(sa.String(20))
    taxpayer_address = sa.Column(sa.String(200))
    taxpayer_id_number = sa.Column(sa.String(12))
    ingredients = sa.Column(sa.Text())
    created_on = sa.Column(sa.TIMESTAMP(), default=datetime.utcnow)
    last_updated_on = sa.Column(sa.TIMESTAMP(), default=datetime.utcnow)


class Cart(Base):

    __tablename__ = 'carts'

    id = sa.Column(sa.String(64), primary_key=True, nullable=False)
    account_id = sa.Column(sa.ForeignKey('accounts.id'), nullable=False)
    product_id = sa.Column(sa.ForeignKey('products.id'), nullable=False)
    options = sa.Column(sa.Text())
    amount = sa.Column(sa.Integer())
    created_on = sa.Column(sa.TIMESTAMP(), default=datetime.utcnow)
    last_updated_on = sa.Column(sa.TIMESTAMP(), default=datetime.utcnow)


class Product(Base):

    __tablename__ = 'products'

    id = sa.Column(sa.String(64), primary_key=True, nullable=False)
    store_id = sa.Column(sa.ForeignKey('stores.id'), nullable=False)
    name = sa.Column(sa.String(100))
    options = sa.Column(sa.Text())
    description = sa.Column(sa.String(500))
    image = sa.Column(sa.String(200))
    price = sa.Column(sa.Integer())
    created_on = sa.Column(sa.TIMESTAMP(), default=datetime.utcnow)
    last_updated_on = sa.Column(sa.TIMESTAMP(), default=datetime.utcnow)


class Order(Base):

    __tablename__ = 'orders'

    id = sa.Column(sa.String(64), primary_key=True, nullable=False)
    account_id = sa.Column(sa.ForeignKey('accounts.id'), nullable=False)
    store_id = sa.Column(sa.ForeignKey('stores.id'), nullable=False)
    status = sa.Column(sa.String(10))
    payment = sa.Column(sa.String(64))
    delivery_type = sa.Column(sa.String(12))
    delivery_id = sa.Column(sa.ForeignKey('deliveries.id'), nullable=False)
    address = sa.Column(sa.String(200))
    phone_number = sa.Column(sa.String(16))
    price = sa.Column(sa.Integer())
    delivery_fee = sa.Column(sa.Integer())
    total_price = sa.Column(sa.Integer())
    virtual_number = sa.Column(sa.String(16))
    wants_disposables = sa.Column(sa.Boolean())
    favor_store = sa.Column(sa.String(100))
    favor_delivery = sa.Column(sa.String(100))
    created_on = sa.Column(sa.TIMESTAMP(), default=datetime.utcnow)
    last_updated_on = sa.Column(sa.TIMESTAMP(), default=datetime.utcnow)


class Alarm(Base):

    __tablename__ = 'alarms'

    id = sa.Column(sa.String(64), primary_key=True, nullable=False)
    account_id = sa.Column(sa.ForeignKey('accounts.id'), nullable=False)
    title = sa.Column(sa.String(100))
    content = sa.Column(sa.String(500))
    link = sa.Column(sa.String(200))
    created_on = sa.Column(sa.TIMESTAMP(), default=datetime.utcnow)
    last_updated_on = sa.Column(sa.TIMESTAMP(), default=datetime.utcnow)


class Orderline(Base):

    __tablename__ = 'orderlines'

    id = sa.Column(sa.String(64), primary_key=True, nullable=False)
    order_id = sa.Column(sa.ForeignKey('orders.id'), nullable=False)
    product_id = sa.Column(sa.ForeignKey('products.id'), nullable=False)
    options = sa.Column(sa.Text())
    amount = sa.Column(sa.Integer())
    created_on = sa.Column(sa.TIMESTAMP(), default=datetime.utcnow)
    last_updated_on = sa.Column(sa.TIMESTAMP(), default=datetime.utcnow)


class Review(Base):

    __tablename__ = 'reviews'

    id = sa.Column(sa.String(64), primary_key=True, nullable=False)
    account_id = sa.Column(sa.ForeignKey('accounts.id'), nullable=False)
    store_id = sa.Column(sa.ForeignKey('stores.id'), nullable=False)
    ratings_delivery = sa.Column(sa.SmallInteger())
    ratings_food = sa.Column(sa.SmallInteger())
    image = sa.Column(sa.String(200))
    content = sa.Column(sa.String(1000))
    reply_id = sa.Column(sa.ForeignKey('replies.id'), nullable=True)
    is_public = sa.Column(sa.Boolean())
    shows_orders = sa.Column(sa.Boolean())
    created_on = sa.Column(sa.TIMESTAMP(), default=datetime.utcnow)
    last_updated_on = sa.Column(sa.TIMESTAMP(), default=datetime.utcnow)


class ReviewTag(Base):

    __tablename__ = 'review_tags'

    id = sa.Column(sa.String(64), primary_key=True, nullable=False)
    review_id = sa.Column(sa.ForeignKey('reviews.id'), nullable=False)
    product_id = sa.Column(sa.ForeignKey('products.id'), nullable=False)
    recommend = sa.Column(sa.Boolean())
    comment = sa.Column(sa.String(100))
    created_on = sa.Column(sa.TIMESTAMP(), default=datetime.utcnow)
    last_updated_on = sa.Column(sa.TIMESTAMP(), default=datetime.utcnow)


class Reply(Base):

    __tablename__ = 'replies'

    id = sa.Column(sa.String(64), primary_key=True, nullable=False)
    content = sa.Column(sa.String(1000))
    created_on = sa.Column(sa.TIMESTAMP(), default=datetime.utcnow)
    last_updated_on = sa.Column(sa.TIMESTAMP(), default=datetime.utcnow)


class Delivery(Base):

    __tablename__ = 'deliveries'

    id = sa.Column(sa.String(64), primary_key=True, nullable=False)
    status = sa.Column(sa.String(10))
    delivery_type = sa.Column(sa.String(12))
    dispatcher_id = sa.Column(sa.ForeignKey('dispatchers.id'), nullable=False)
    created_on = sa.Column(sa.TIMESTAMP(), default=datetime.utcnow)
    last_updated_on = sa.Column(sa.TIMESTAMP(), default=datetime.utcnow)


class Dispatcher(Base):

    __tablename__ = 'dispatchers'

    id = sa.Column(sa.String(64), primary_key=True, nullable=False)
    status = sa.Column(sa.String(10))
    name = sa.Column(sa.String(20))
    dispatcher_ride = sa.Column(sa.String(20))
    phone_number = sa.Column(sa.String(16))
    virtual_number = sa.Column(sa.String(16))
    agency_id = sa.Column(sa.ForeignKey('agencies.id'), nullable=False)
    created_on = sa.Column(sa.TIMESTAMP(), default=datetime.utcnow)
    last_updated_on = sa.Column(sa.TIMESTAMP(), default=datetime.utcnow)


class StoreCategory(Base):

    __tablename__ = 'store_categories'

    id = sa.Column(sa.String(64), primary_key=True, nullable=False)
    store_id = sa.Column(sa.ForeignKey('stores.id'), nullable=False)
    category_id = sa.Column(sa.ForeignKey('categories.id'), nullable=False)
    created_on = sa.Column(sa.TIMESTAMP(), default=datetime.utcnow)
    last_updated_on = sa.Column(sa.TIMESTAMP(), default=datetime.utcnow)


class Category(Base):

    __tablename__ = 'categories'

    id = sa.Column(sa.String(64), primary_key=True, nullable=False)
    parent_category_id = sa.Column(sa.ForeignKey('categories.id'), nullable=True)
    name = sa.Column(sa.String(20))
    description = sa.Column(sa.String(100))
    created_on = sa.Column(sa.TIMESTAMP(), default=datetime.utcnow)
    last_updated_on = sa.Column(sa.TIMESTAMP(), default=datetime.utcnow)


class Agency(Base):

    __tablename__ = 'agencies'

    id = sa.Column(sa.String(64), primary_key=True, nullable=False)
    name = sa.Column(sa.String(100))
    created_on = sa.Column(sa.TIMESTAMP(), default=datetime.utcnow)
    last_updated_on = sa.Column(sa.TIMESTAMP(), default=datetime.utcnow)


class DeliveryInformation(Base):

    __tablename__ = 'delivery_informations'

    id = sa.Column(sa.String(64), primary_key=True, nullable=False)
    store_id = sa.Column(sa.ForeignKey('stores.id'), nullable=True)
    delivery_type = sa.Column(sa.String(12))
    min_fee = sa.Column(sa.Integer())
    max_fee = sa.Column(sa.Integer())
    created_on = sa.Column(sa.TIMESTAMP(), default=datetime.utcnow)
    last_updated_on = sa.Column(sa.TIMESTAMP(), default=datetime.utcnow)


class OrderStatus(Base):

    __tablename__ = 'order_status'

    id = sa.Column(sa.String(64), primary_key=True, nullable=False)
    order_id = sa.Column(sa.ForeignKey('orders.id'), nullable=True)
    progress = sa.Column(sa.String(10))
    dispatcher_location = sa.Column(sa.String(200))
    dispatcer_latitude = sa.Column(sa.Numeric())
    dispatcer_longtitude = sa.Column(sa.Numeric())
    created_on = sa.Column(sa.TIMESTAMP(), default=datetime.utcnow)
    last_updated_on = sa.Column(sa.TIMESTAMP(), default=datetime.utcnow)
