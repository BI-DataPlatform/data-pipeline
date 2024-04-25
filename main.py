from utils.RandomGenerator import *
from domain.Account import Account
from domain.FamilyAccount import FamilyAccount
from domain.Address import Address
import pandas as pd
import sqlalchemy

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
    accounts = []
    family_accounts = []
    addresses = []
    address_table = get_address_table('./utils/주소.xlsx')
    
    for i in range(rows):
        # make account
        account = Account(
            email=generate_email(),
            password=generate_pw(),
            nickname=generate_name(),
            phone_number=generate_phone(),
            virtual_number=generate_virtual_number())
        
        # df 생성을 위해 dict list에 추가
        accounts.append(account.to_dict())
        
        # make familly_account
        family = randint(0,8)
        if family == 0:
            family_account = FamilyAccount(
                account_id=account.id, 
                orders_left=randint(0,10))
            account.family_account_id = family_account.id
            family_accounts.append(family_account.to_dict())
        elif family ==1 and len(family_accounts) != 0:
            family_account = family_accounts[randint(0, len(family_accounts)-1)]
            account.family_account_id = family_account['id']
        else: family_account = "no familiy account"
        
        
        # make addresses
        add_address = randint(0,5)
        if add_address ==0 :
            address_data = address_table[randint(0,len(address_table)-1)]
            address = Address(
                account_id= account.id,
                is_current= randint(0,1)==0,
                name = generate_address_name(),
                first_address = address_data[0]+' '+address_data[1],
                second_address = address_data[2]
            )
            addresses.append(address.to_dict())
        else:
            address = "no address"
            
        # print('-------')
        # print(account)
        # print(family_account)
        # print(address)
        # print('-------')

    # 객체 리스트를 dataframe으로 변환하여 sql 실행
    account_df = pd.DataFrame(accounts)
    family_account_df = pd.DataFrame(family_accounts)
    address_df = pd.DataFrame(addresses)
    # print(account_df)
    # print(family_account_df)
    # print(address_df)

    account_df.to_sql(name='accounts', con=connection, index=False, if_exists='append')
    family_account_df.to_sql(name='family_accounts', con=connection, index=False, if_exists='append')
    address_df.to_sql(name='addresses', con=connection, index=False, if_exists='append')

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