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
        return generate_phone
    else: 
        return ''
