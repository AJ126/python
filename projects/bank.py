import sys
class Customer:
    bankname='AkashBank'
    def __init__(self,name,balance=0.0):
         self.name=name
         self.balance=balance
    def deposit(self,amt):
        self.balance=self.balance+amt
        print('balance after deposit:', self.balance)
    def withdraw(self,amt):
        if amt>self.balance:
            print('insufficient founds..')
            sys.exit()
        self.balance=self.balance-amt
        print('current balance is :',self.balance)
print('welcome to', Customer.bankname)
name=input('enter your name: ')
c=Customer(name)
while True:
    print('d-Deposit \ w-withdraw \ e-exit')
    option=input('choose your option: ')
    if option=='d' or option=='D':
        amt=float(input('Enter Amount : '))
        c.deposit(amt)
    elif option=='w' or option=='W':
        amt=float(input('Enter Amount : '))
        c.withdraw(amt)
    elif option=='e' or option=='E':
        print('thank you banking')
        sys.exit()
    else:
        print('invalid option ...')
