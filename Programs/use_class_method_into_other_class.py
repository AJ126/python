# Passing members of one class to another class
class demo:
    def __init__(self, name, address):
        self.name = 'shiv'
        self.address = address
    def showVal(self):
        print('user name: ', self.name)
        print('user address: ', self.address)
				
class test:
    def show(data):
        data.address = 'kailash parvat'
        print('show value', data)
        data.showVal()		
d = demo('shiv', 'kailash')
test.show(d)