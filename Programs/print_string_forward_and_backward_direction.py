string = str(input("Enter a string: "))
length = len(string)
print("The length of the string is:", length)
print("the -ve length of the string is:", -length)
i=0
print("The string in forward direction is:", string)
while i<length:
    print(string[i], end="")
    i+=1
print("\nThe string in backward direction is:", string)
i=-1
while i>=-length:
    print(string[i], end="")
    i-=1

# by using slicing
# for i in string:
#     print(i,end=' ')
# print("\nThe string in forward direction is:", string)
# for i in string[::]:
#     print(i,end=' ')

# print("\nThe string in backward direction is:", string)
# for i in string[::-1]:
#     print(i,end=' ')