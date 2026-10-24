import datetime
today=datetime.datetime.now()
s=repr(today)
print(s)
print('using repr method we can convert str to orignal object')
a=eval(s)
print(a)
