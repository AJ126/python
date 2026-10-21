# Write a program to reverse the given String

string = input("Enter a string: ")
# first method to reverse the string
print("The reversed string is:", string[::-1])
# second method to reverse the string
print("The reversed string is:", ''.join(reversed(string)))
# third method to reverse the string
i = len(string) - 1
target = ""
while i >= 0:
    target += string[i]
    i -= 1
print("The reversed string is:", target)


# Program to reverse order of words.
# output = mahadev har har
value = 'har har mahadev'
s = value.split() # split the string into words
a = []
i = len(s) - 1
while i >= 0:
    a.append(s[i]) # append the words in reverse order
    i -= 1
print("The reversed order of words is:", ' '.join(a))
