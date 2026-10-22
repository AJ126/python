list = ['shiv', 'mahadev', 'vishnu', 'ganesh', 'kali', 'durga', 'krishna', 'rama', 'hanuman', 'parvati']

#print the list using indexing
print(list[0])  # Output: shiv

#print the list using slicing
print(list[1:3])  # Output: ['mahadev', 'vishnu']
print(list[:2])  # Output: ['shiv', 'mahadev']
print(list[0:3:1])  # Output: ['shiv', 'mahadev', 'vishnu']

# update the list using indexing
list[1] = 'rudra'
print(list)  # Output: ['shiv', 'rudra', 'vishnu']

# get the length of the list
print(len(list))  # Output: 10

# check the items count in the list
print(list.count('shiv'))  # Output: 1

# index function to get the index of an item in the list
# return the index of the first occurrence of the item in the list
print(list.index('vishnu'))  # Output: 2

## append function to add an item to the end of the list
list.append('lakshmi')
print(list)  # Output: ['shiv', 'rudra', 'vishnu', 'ganesh', 'kali', 'durga', 'krishna', 'rama', 'hanuman', 'parvati', 'lakshmi']


# insert function to add an item at a specific index in the list
list.insert(2, 'narayan')
print(list)  # Output: ['shiv', 'rudra', 'narayan', 'vishnu', 'ganesh', 'kali', 'durga', 'krishna', 'rama', 'hanuman', 'parvati', 'lakshmi']

#  If the specified index is greater than max index then element will be inserted at last
# position. If the specified index is smaller than min index then element will be inserted at
# first position.

# extend function to add multiple items to the end of the list
# add one list items into another list
l = ['saraswati', 'lakshmi']
list.extend(l)
print(list)  # Output: ['shiv', 'rudra', 'narayan', 'vishnu', 'ganesh', 'kali', 'durga', 'krishna', 'rama', 'hanuman', 'parvati', 'lakshmi', 'saraswati', 'lakshmi']

# remove function to remove an item from the list
# remove specified item from the list.If the item present multiple times then only first 
# occurrence will be removed
# remove funtion cant return any value. If the item is not present in the list then it will throw ValueError
list.remove('lakshmi')
print(list)  # Output: ['shiv', 'rudra', 'narayan', 'vishnu', 'ganesh', 'kali', 'durga', 'krishna', 'rama', 'hanuman', 'parvati', 'saraswati']

# pop function to remove an item from the list based on index
# If index is not specified then last item will be removed from the list
# pop function return the removed item from the list. If the index is not present in the list then it will throw IndexError

list.pop()
print(list)  # Output: ['shiv', 'rudra', 'narayan', 'vishnu', 'ganesh', 'kali', 'durga', 'krishna', 'rama', 'hanuman', 'parvati', 'saraswati']

list.pop(2)
print(list)  # Output: ['shiv', 'rudra', 'vishnu', 'ganesh', 'kali', 'durga', 'krishna', 'rama', 'hanuman', 'parvati', 'saraswati']


# reverse function to reverse the list
list.reverse()
print(list)  # Output: ['saraswati', 'parvati', 'hanuman', 'rama', 'krishna', 'durga', 'kali', 'ganesh', 'vishnu', 'rudra', 'shiv']

# sort function to sort the list in ascending order
list.sort()
print(list)  # Output: ['durga', 'ganesh', 'hanuman', 'kali', 'krishna', 'parvati', 'rudra', 'shiv', 'saraswati', 'vishnu']


# sort function to sort the list in descending order
list.sort(reverse=True)
print(list)  # Output: ['vishnu', 'saraswati', 'shiv', 'rudra', 'parvati', 'krishna', 'kali', 'hanuman', 'ganesh', 'durga']

# clear function to remove all items from the list
list.clear()
print(list)  # Output: []

# aliasing a list to another variable
list1 = ['shiv', 'rudra', 'vishnu', 'ganesh', 'kali', 'durga', 'krishna', 'rama', 'hanuman', 'parvati']
list2 = list1
print(list2)  # Output: ['shiv', 'rudra', 'vishnu', 'ganesh', 'kali', 'durga', 'krishna', 'rama', 'hanuman', 'parvati']

# problem in aliasing is if we change the list1 then list2 will also be changed because both are pointing to the same memory location
# so overcome this problem we can use clone function to create a copy of the list

# clone function to create a copy of the list
list1 = ['shiv', 'rudra', 'vishnu', 'ganesh', 'kali', 'durga', 'krishna', 'rama', 'hanuman', 'parvati']
# clone function to create a copy of the list using copy() method
list2 = list1.copy()
print(list2)  # Output: ['shiv', 'rudra', 'vishnu', 'ganesh', 'kali', 'durga', 'krishna', 'rama', 'hanuman', 'parvati']

# clone function to create a copy of the list using slicing
list3 = list1[:]
print(list3)  # Output: ['shiv', 'rudra', 'vishnu', 'ganesh', 'kali', 'durga', 'krishna', 'rama', 'hanuman', 'parvati']

# concatenate two lists using + operator
list4 = list1 + list2
print(list4)  # Output: ['shiv', 'rudra', 'vishnu', 'ganesh', 'kali', 'durga', 'krishna', 'rama', 'hanuman', 'parvati', 'shiv', 'rudra', 'vishnu', 'ganesh', 'kali', 'durga', 'krishna', 'rama', 'hanuman', 'parvati']

# concatenate two lists using extend() method
list1.extend(list2)
print(list1)  # Output: ['shiv', 'rudra', 'vishnu', 'ganesh', 'kali', 'durga', 'krishna', 'rama', 'hanuman', 'parvati', 'shiv', 'rudra', 'vishnu', 'ganesh', 'kali', 'durga', 'krishna', 'rama', 'hanuman', 'parvati']

# repeat a list using * operator
list5 = list1 * 2
print(list5)  # Output: ['shiv', 'rudra', 'vishnu', 'ganesh', 'kali', 'durga', 'krishna', 'rama', 'hanuman', 'parvati', 'shiv', 'rudra', 'vishnu', 'ganesh', 'kali', 'durga', 'krishna', 'rama', 'hanuman', 'parvati', 'shiv', 'rudra', 'vishnu', 'ganesh', 'kali', 'durga', 'krishna', 'rama', 'hanuman', 'parvati']

# nested list
nested_list = [['shiv', 'rudra', 'vishnu'], ['ganesh', 'kali', 'durga'], ['krishna', 'rama', 'hanuman', 'parvati']]
print(nested_list)  # Output: [['shiv', 'rudra', 'vishnu'], ['ganesh', 'kali', 'durga'], ['krishna', 'rama', 'hanuman', 'parvati']] 






