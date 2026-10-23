class test:
    def __init__(self):
        print('parent init')
    def check(self):
        print('check the test')

    def price(self):
        print('price 50')

class testing(test):
    def __init__(self): # constructor overloading
            print('child init')
    def price(self):
        print('price from testing (child) 70')
        return super().price() # return the parent class method output

t = testing()
t.check()
t.price()