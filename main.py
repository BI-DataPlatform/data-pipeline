from utils.RandomGenerator import *
from domain.Account import Account
from domain.FamilyAccount import FamilyAccount


if __name__ == '__main__':
    family_accounts = []
    for i in range(10):
        account = Account(
            email=generate_email(),
            password=generate_pw(),
            nickname=generate_name(),
            phone_number=generate_phone(),
            virtual_number=generate_virtual_number())
        
        family = randint(0,2)
        if family == 0:
            family_account = FamilyAccount(
                account_id=account.id, 
                orders_left=random_int())
            account.family_account_id = family_account.id
            family_accounts.append(family_account.id)
        elif family ==1 and len(family_accounts) != 0:
            account.family_account_id = family_accounts[random_int(0, len(family_accounts)-1)]
            family_account=account.family_account_id
        else: family_account= None
        
        print('-------')
        print(account)
        print(family_account)
        print('-------')
