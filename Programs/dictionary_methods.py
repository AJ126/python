# create empty dictionary
my_dict = {}
my_dict1 = dict()

# add items in the dictionary
my_dict['name'] = 'shiv'
print(my_dict)

# Access data from dictionary
print(my_dict['name'])

# update dictionary
my_dict['name'] = 'mahadev'
# if related key is not available then it will create a new item, 
# if key available then update the value

# delete items from dictionary
del my_dict['address']

# delete all items from dictionary
my_dict.clear()

# delete dictionary 
del my_dict

# length of dictionary, return the number of items in the list
print(len(my_dict))

# clear , remove all items from disctionary
my_dict.clear()

# get,  get the value associated with the key
value = my_dict.get('name')
value = my_dict.get('name', 'shiv') # return a name value if value is not present then return default value default value is 'shiv'

# pop remove the key value from list, return the deleted key value
# If the specified key is not available then we will get KeyError
print(my_dict.pop('number'))

# popitem function remove the fisr key value pair 
# If the dictionary is empty then we will get KeyError
print(my_dict.popitem())

#  keys() fuunction return all keys from dictionary
print(my_dict.keys())

# values() It returns all values associated with the dictionary
print(my_dict.values())

# items() It returns list of tuples representing key-value pairs

print(my_dict.items())

# copy() function To create exactly duplicate dictionary(cloned copy)
dictValue = my_dict.copy()

# setdefault() function if the key is already available then this function returns the corresponding value.
# If the key is not available then the specified key-value will be added as new item to the  dictionary.

my_dict.setdefault('name', 'shiv')

# update() function 







