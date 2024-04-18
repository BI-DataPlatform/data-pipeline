from utils.RandomGenerator import *
from domain.Account import Account
from domain.FamilyAccount import FamilyAccount
from domain.Address import Address
from services import MySQLConnection

if __name__ == '__main__':
    DATA_ROWS=1
    
    
    family_accounts = []
    address_table = get_address_table('./utils/주소.xlsx')
    
    for i in range(DATA_ROWS):
        # make account
        account = Account(
            email=generate_email(),
            password=generate_pw(),
            nickname=generate_name(),
            phone_number=generate_phone(),
            virtual_number=generate_virtual_number())
        
        
        # make familly_account
        family = randint(0,10)
        if family == 0:
            family_account = FamilyAccount(
                account_id=account.id, 
                orders_left=randint(0,10))
            account.family_account_id = family_account.id
            family_accounts.append(family_account.id)
        elif family ==1 and len(family_accounts) != 0:
            account.family_account_id = family_accounts[randint(0, len(family_accounts)-1)]
            family_account=account.family_account_id
        else: family_account= "no familiy account"
        
        
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
        else:
            address = "no address"
            
        print('-------')
        print(account)
        print(family_account)
        print(address)
        print('-------')

    engine = MySQLConnection.get_connection()
    