# Write a program to accept student name and marks from the keyboard
# and creates a dictionary. Also display student marks by taking student name
# as input

num = int(input('Enter the number of student:'))
d = {}
for i in range(num):
    name = str(input('Enter the name of student:'))
    mark = float(input('Enter the mark of student:'))
    d[name]=mark
while True:
    name = str(input('Enter the student name to search for marks:'))
    mark = d.get(name, -1)
    if mark == -1:
        print('student not found')
    else:
        print('The mark of', name, 'are', mark)
    option = str(input('Do you want to find another student info [Yes/No]: '))
    if option.lower() != 'yes':
        break;
print('Thank You')