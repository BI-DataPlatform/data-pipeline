from random import *
import string
from korean_name_generator import namer

def generate_name():
    if randint(0, 1)==0:    
        # 남자 이름 생성
        return namer.generate(True)
    else:
        # 여자 이름 생성
        return namer.generate(False)

def generate_phone():
    return '010' + str(int(random() * 100000000))

def generate_email():
    return ''.join(choice(string.ascii_letters) for _ in range(12)) + "@test.com"

def generate_pw():
    lowercase_letters = string.ascii_lowercase
    digits = string.digits
    uppercase_letters = string.ascii_uppercase
    lowercase = ''.join(choice(lowercase_letters) for _ in range(5))
    numbers = ''.join(choice(digits) for _ in range(3))
    uppercase = ''.join(choice(uppercase_letters) for _ in range(2))
    return lowercase+numbers+uppercase 

def generate_virtual_number():
    if randint(0, 1)==0:
        return generate_phone()
    else: 
        return ''
    
def generate_address_name():
    word_set = ['집','학교','회사','기타']
    return word_set[randint(0,3)]

def get_address_table(file_name):
    import pandas as pd
    df = pd.read_excel(file_name)
    df = df[['시도명', '시군구명','읍면동명']].drop_duplicates().dropna()
    # print(df)
    # print(df.to_dict(orient='split')['data'])
    return df.to_dict(orient='split')['data']
    
    
if __name__ == '__main__':
    # utils 폴더로 이동 후 실행해서 excel 파일 잘 읽었나 테스트
    get_address_table()