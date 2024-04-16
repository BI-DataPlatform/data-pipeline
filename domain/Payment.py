from random import randint

def get_payment():
    payment = ['naverPay', 'card', 'kakaoPay', 'payco', 'toss', 'kcp'] # kcp : korea cyber payment의 약자. 은행 계좌를 뜻함.
    return payment[randint(0, len(payment)-1)]
    

