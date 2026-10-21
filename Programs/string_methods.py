value = str(input("Enter a value: "))

#printing the value by indexing +ve and -ve indexing
print("The value is:", value[0])
print("The value is:", value[-1])

# printing the value by slicing
print("The value is:", value[0:3])
print("The value is:", value[1:4:2]) # start index, end index, step
print("The value is:", value[::]) # print entire string
print("The value is:", value[:]) # print entire string
print("The value is:", value[::-1]) # print entire string in reverse order

# printing the value by adding a string to the value
print("The value is:", value + "Har Har Mahadev")

# printing the value by multiplying the value
print("The value is:", value * 3)

# printing the value by using the len() function
print("The length of the value is:", len(value))

# checking 'shiv' in the value
if 'shiv' in value:
    print("Yes, 'shiv' is present in the value")
else:
    print("No, 'shiv' is not present in the value")

# checking 'Akash' not in the value
if 'Akash' not in value:
    print("Yes, 'Akash' is not present in the value")

# removing the leading and trailing spaces from the value
a = value.strip() # remove spaces from both ends
print("The value after removing leading and trailing spaces is:", a)

b = value.lstrip() # remove spaces from left end
print("The value after removing leading spaces is:", b)

c = value.rstrip() # remove spaces from right end
print("The value after removing trailing spaces is:", c)

# find the substring in the value
d = value.find('shiv') # find the substring 'shiv' in the value, find value in forward direction
print("The index of the substring 'shiv' in the value is:", d) 

c = value.rfind('shiv') # find the substring 'shiv' in the value, find value in backward direction
print("The index of the substring 'shiv' in the value is:", c)

# finding the index of the substring in the value
e = value.index('shiv') # find the index of the substring 'shiv' in the value, find value in forward direction
print("The index of the substring 'shiv' in the value is:", e)

f = value.rindex('shiv') # find the index of the substring 'shiv' in the value, find value in backward direction
print("The index of the substring 'shiv' in the value is:", f)

# counting the number of occurrences of the substring in the value
g = value.count('shiv') # count the number of occurrences of the substring 'shiv' in the value
print("The number of occurrences of the substring 'shiv' in the value is:", g)

# replacing the substring in the value
h = value.replace('shiv', 'Mahadev') # replace the substring 'shiv' with 'Mahadev' in the value
print("The value after replacing the substring 'shiv' with 'Mahadev' is:", h)

# splitting the value into a list of substrings
i = value.split() # split the value into a list of substrings
print("The value after splitting into a list of substrings is:", i)

# joining the list of substrings into a single string
j = ' '.join(i) # join the list of substrings into a single string
print("The value after joining the list of substrings into a single string is:", j)

# changing the case of the value
k = value.upper() # change the case of the value to upper case
print("The value after changing the case to upper case is:", k)

l = value.lower() # change the case of the value to lower case
print("The value after changing the case to lower case is:", l)

m = value.title() # change the case of the value to title case
print("The value after changing the case to title case is:", m)

n = value.capitalize() # change the case of the value to capitalize case
print("The value after changing the case to capitalize case is:", n)

o = value.swapcase() # change the case of the value to swap case
print("The value after changing the case to swap case is:", o)

# checking the start and end of the value
p = value.startswith('shiv') # check if the value starts with 'shiv'
print("Does the value start with 'shiv'?:", p)

q = value.endswith('shiv') # check if the value ends with 'shiv'
print("Does the value end with 'shiv'?:", q)

# checking if the value is alphanumeric, alphabetic, digit, decimal, space, lower case, upper case, title case
r = value.isalnum() # check if the value is alphanumeric
print("Is the value alphanumeric?:", r)

s = value.isalpha() # check if the value is alphabetic
print("Is the value alphabetic?:", s)

t = value.isdigit() # check if the value is a digit
print("Is the value a digit?:", t)

u = value.isdecimal() # check if the value is a decimal
print("Is the value a decimal?:", u)

v = value.isspace() # check if the value is a space
print("Is the value a space?:", v)

w = value.islower() # check if the value is in lower case
print("Is the value in lower case?:", w)

x = value.isupper() # check if the value is in upper case
print("Is the value in upper case?:", x)

y = value.istitle() # check if the value is in title case
print("Is the value in title case?:", y)

# formatting the value
title = 'Har Har Mahadev'
name = 'Shiv'
print("The value is: {} {}".format(title, name)) # using format() method
print(f"The value is: {title} {name}") # using f-string



