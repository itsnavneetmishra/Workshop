#Encapsulation

"""Wrapping data and functions into a single unit (object)"""

"""Create Account class with 2 attributes -balance and account number
Create methods for debit, credit and printing the balance"""


class Account:
    def __init__(self,bal,acc):
        self.bal=bal
        self.acc=acc



    #debit method

    def debit(self,amount):
        self.bal=-amount
        print("Rs",amount,"was debited")


    def credit(self,amount):
        self.bal=+amount
        print("Rs",amount,"was credited")

    def get_bal(self):
        print("your account balance",self.bal)


acc1= Account(10000,12345)

acc1.debit(1000)

acc1.credit(9999)


acc1.get_bal()
