# -*- coding: utf-8 -*-

from domain.Order import Order
from domain.OrderStatus import OrderStatus
from domain.Delivery import Delivery
import pandas as pd
import sqlalchemy
from faker import Faker

import time # 실행 시간 측정용
from memory_profiler import profile # 메모리 측정용

def get_engine():
    id = 'root'
    passwd = 'root'
    host ='192.168.122.110'
    port = '30829'
    db = 'data'
    return sqlalchemy.create_engine("mysql+pymysql://" + id + ":" + passwd + "@" 
                                    + host + ":" + port + "/" + db+'?charset=utf8mb4')

def create_schema(connection: sqlalchemy.Connection):
    # schema.sql 파일 읽기
    with open('./schema.sql', 'r') as file:
        queryies = file.read().split(';')
    
    # 공백 제거
    queryies = [q for q in queryies if q.strip()]
    
    # ddl 실행 : mysql은 한번에 한 쿼리만 실행 가능해서 for문으로 돌림.
    for query in queryies:
        connection.execute(sqlalchemy.text(query))
    
    connection.close()

@profile
def generate_data(rows, connection: sqlalchemy.Engine):
    # todo: id 목록 받아오는 과정 개선
    with engine.connect() as conn:
        account_query = "SELECT id FROM account;"
        account_ids_df = pd.read_sql(account_query, conn)

        store_query = "SELECT id FROM store;"
        store_ids_df = pd.read_sql(store_query, conn)

        delivery_query = "SELECT id, delivery_type FROM delivery;"
        deliveries_df = pd.read_sql(delivery_query, conn)

        order_query = "SELECT id FROM order;"
        order_df = pd.read_sql(order_query, conn)

    account_ids = account_ids_df["id"].tolist()
    store_ids = store_ids_df["id"].tolist()
    deliveries = deliveries_df.tolist()
    order_ids = order_df["id"].tolist()
    
    statuses = ["Requesting", "Accepted", "Cooking", "Cooking Completed", "Delivering", "Delivered", "Cancelled"]
    payments = ["baemin", "credit", "toss", "etc"]
    
    orders = []
    for i in range(rows):
        phone_number = f"010-{randint(1000, 9999)}-{randint(1000, 9999)}"
        price = randint(3000, 100000)
        delivery_fee = randint(0, 10000)
        total_price = price + delivery_fee
        delivery = random.choice(deliveries)

        wants_disposable = random.choice([True, False])
        if wants_disposable:
            virtual_number = f"050-{randint(1000, 9999)}-{randint(1000, 9999)}"
        else:
            virtual_number = None

        order = Order(
            account_id = random.choice(account_ids),
            store_id = random.choice(store_ids),
            status = random.choice(statuses),
            payment = random.choice(payments),
            delivery_id = delivery["id"],
            delivery_type = delivery["delivery_type"],
            address = fake.address(),
            phone_number = phone_number,
            price = price,
            delivery_fee = delivery_fee,
            total_price = total_price,
            wants_disposable = wants_disposable,
            virtual_number = virtual_number,
            favor_store = fake.sentence(),
            favor_delivery = fake.sentence(),
        )

        orders.append(order.to_dict())
    df_orders = pd.DataFrame(orders)

    orderStatuses = []
    for _ in range(rows):
        orderStatus = OrderStatus(
            order_id = random.choice(order_ids),
            progress = random.choice(statuses),
            dispatcher_location = fake.address(),
            dispatcher_latitude = str(fake.latitude()),
            dispatcher_longitude = str(fake.longitude()),
        )

        orderStatuses.append(orderStatus.to_dict())
    df_orderStatus = pd.DataFrame(orderStatuses)


    deliveries = []
    delivery_types = ["car", "bike", "walk", "motorcycle"]
    for _ in range(rows):
        delivery = Delivery(
            status = random.choice(statuses),
            delivery_type = random.choice(delivery_types),
        )

        deliveries.append(delivery.to_dict())
    df_delivery = pd.DataFrame(deliveries)

    df_orders.to_sql(name='order', con=connection, index=False, if_exists='append')
    df_orderStatus.to_sql(name='orderStatus', con=connection, index=False, if_exists='append')
    df_delivery.to_sql(name='delivery', con=connection, index=False, if_exists='append')

if __name__ == '__main__':
    
    # 시작 시간 기록
    start_time = time.time()
    
    DATA_ROWS=30000
    
    engine = get_engine()
    
    # 테이블 생성 및 기본 키 설정
    create_schema(engine.connect())
    
    # 데이터 생성 및 메모리 사용량 추적
    generate_data(DATA_ROWS, engine)
    engine.dispose()
    
    # 종료 시간 기록
    end_time = time.time()

    # 실행 시간 계산
    execution_time = end_time - start_time
    print("Execution time:", execution_time, "seconds")