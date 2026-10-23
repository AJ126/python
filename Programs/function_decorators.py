
def decoratorsName(func):
    def name(n):
        if n == 'Shiv':
            print('har har mahadev')
        else:
            func(name)
    return name

@decoratorsName
def printname(name):
    print('om namaha shivya')

printname('Shiv')
printname('mahadev')
