class human:
    def talk(self):
        print('har har mahadev')

class lion:
    def talk(self):
        print('drow  drow')

class tiger:
    def talk(self):
        print('tiger drow drow')

class bull:
    def talk(self):
        print('hama hama')

class elephant:
    def talk(self):
        print('elephant haan haan')

def show(obj):
    obj.talk()
l = [human(), lion(), tiger(), bull(), elephant()]
for obj in l:
    show(obj)