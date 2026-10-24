class claculator:
    def __init__(self,x,y,opt):
        self.x=x
        self.y=y
        self.opt=opt
    def show(self):
        if self.opt=='+':
            a=self.x+self.y
            print('addition of ',self.x,' and ',self.y,' is ',a)
        elif opt=='-':
            b=self.x-self.y
            print('subtraction of ',self.x,' and ',self.y,' is ',b)
        elif opt=='*':
            c=self.x*self.y
            print('multiplication of ',self.x, ' and ',self.y,' is ',c)
        elif opt=='/':
            b=self.x/self.y
            print('devision of ',self.x,' and ',self.y,' is ',b)
        elif opt=='**':
            c=self.x**self.y
            print('exponent of ',self.x, ' and ',self.y,' is ',c)
        elif opt=='//':
            c=self.x//self.y
            print('floor devision of ',self.x, ' and ',self.y,' is ',c)
        else:
            print('please enter valid number')
print()
print('you can perform +, -, *, /, **, // operations choose any one')
print()
x=eval(input('enter first no :'))
opt=input('enter which operation you want to perform :')
y=eval(input('enter second no :'))
c=claculator(x,y,opt)
c.show()
