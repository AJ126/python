class test:
    def __init__(self):
        print('parent class init')
    def show(self):
        print('parent class method')
    class demo:
        def __init__(self):
            print('child class init')
        def showchild(self):
            print('child class method')

t = test()
t.show()
child = t.demo()
child.showchild()