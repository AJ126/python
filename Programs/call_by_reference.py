def f(a):
    a[0]=300
    a[1]=400
b=[30,20]
f(b) # function call by reference
print(b)