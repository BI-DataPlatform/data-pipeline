from utils.RandomGenerator import *
from domain.Account import Account



if __name__ == '__main__':
    account = Account(
        email=generate_email(),
        password=generate_pw(),
        nickname=generate_name(),
        phone_number=generate_phone())
    print(account)