# Write a program to create a lambda function to find square of given number

s=lambda v:v*v
print(s(2)) # output : 4

# Lambda function to find sum of 2 given numbers
sum = lambda a, b: a+b

print(sum(2,5)) # output: 7

# Lambda Function to find biggest of given values.
big = lambda a, b: a if a> b else b

print('big number is', big(10, 50)) # output: big number is 50

#  Program to filter only even numbers from the list by using filter() function

listvalue = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
list1 = list(filter(lambda x: x % 2 == 0, listvalue))
print(list1) # output: [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]