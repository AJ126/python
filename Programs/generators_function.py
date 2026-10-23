import random
import time

def count(num):
    while num > 0:
        yield num
        num = num -1

value = count(5)
for x in value:
    print('number', x)

name = ['shiv', 'mahadev', 'rudra', 'vishnu', 'parvati', 'laxmi']
power = ['all', 'palan', 'shakti', 'money']

def listVal(num):
    result = []
    for i in range(num):
        god = {
            'id': i,
            'name': random.choice(name),
            'power': random.choice(power)
        }
        result.append(god)
    return result

timeVal = time.perf_counter()
god = listVal(10000)
timeVal2 = time.perf_counter()
print(f'List execution time: {timeVal2 - timeVal:.6f} seconds')

def generatList(num):
    for i in range(num):
        god = {
            'id': i,
            'name': random.choice(name),
            'second power': random.choice(power)
        }
        yield god

timeVal = time.perf_counter()
god = generatList(10000)
timeVal2 = time.perf_counter()
print(f'List execution time: {timeVal2 - timeVal:.6f} seconds')