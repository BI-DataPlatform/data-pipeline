from utils.RandomGenerator import *
from domain.Account import Account
from domain.FamilyAccount import FamilyAccount
from domain.Address import Address
import pandas as pd
import sqlalchemy

def get_connection():
    id = 'root'
    passwd = 'root'
    host ='192.168.122.110'
    port = '30829'
    db = 'data'
    return sqlalchemy.create_engine("mysql+pymysql://" + id + ":" + passwd + "@" 
                                    + host + ":" + port + "/" + db+'?charset=utf8mb4')

# class to ddl 자동 생성 해보려고했는데 varchar length 자동 지정이 안되어서 포기
# def generate_table_create_query(class_type):
#     columns = []
#     for field in class_type.__dataclass_fields__.values():
#         if field.name == 'email':
#             max_length = 50 
#         elif field.name == 'name' :
#             max_length = 20
#         else : 
#             max_length = 64
#         columns.append(f"{field.name} {get_sqlalchemy_type(field.type, max_length)}")
#     return f"CREATE TABLE {class_type.__name__.lower()} ({', '.join(columns)});"

# def get_sqlalchemy_type(data_type, max_length=None):
#     if data_type == int:
#         return "INTEGER"
#     elif data_type == str:
#         if max_length:
#             return f"VARCHAR({max_length})"
#         else:
#             return "TEXT"
#     elif data_type == bool:
#         return "BOOLEAN"
#     else:
#         raise ValueError(f"Unsupported data type: {data_type}")

def create_schema(engine: sqlalchemy.Engine):
    # schema.sql 파일 읽기
    with open('./schema.sql', 'r') as file:
        queryies = file.read().split(';')
    
    # 공백 제거
    queryies = [q for q in queryies if q.strip()]
    
    # ddl 실행 : mysql은 한번에 한 쿼리만 실행 가능해서 for문으로 돌림.
    for query in queryies:
        engine.connect().execute(sqlalchemy.text(query))

if __name__ == '__main__':
    DATA_ROWS=10000
    
    engine = get_connection()
    
    # 테이블 생성 및 기본 키 설정
    create_schema(engine)
        
    accounts = []
    family_accounts = []
    addresses = []
    address_table = get_address_table('./utils/주소.xlsx')
    
    for i in range(DATA_ROWS):
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

    account_df.to_sql(name='accounts', con=engine, index=False, if_exists='append')
    family_account_df.to_sql(name='family_accounts', con=engine, index=False, if_exists='append')
    address_df.to_sql(name='addresses', con=engine, index=False, if_exists='append')
    
