class student:
    def __init__(self, name, address, phone):
        self.name = name
        self.address = address
        self.phone = phone
    def show(self):
        print('student name is:', self.name)
        print('student address is:', self.address)
        print('student phone is:', self.phone)

s = student('shiv', 'kailash parvat', '8888120866')
s.show()