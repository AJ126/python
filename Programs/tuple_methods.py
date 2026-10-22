# create a empty tuple
empty_tuple = ()
print("Empty tuple:", empty_tuple)

# create a tuple with single element
# when creating a tuple with a single element, we need to add a comma after the element to 
# differentiate it from a regular parenthesis
single_element_tuple = (5,)
print("Single element tuple:", single_element_tuple)

# create a tuple by using the tuple() constructor
list = [1, 2, 3, 4, 5]
tuple_from_list = tuple(list)
print("Tuple from list:", tuple_from_list)

# accessing elements in a tuple using indexing
my_tuple = (10, 20, 30, 40, 50)
print("First element:", my_tuple[0])  # Output: 10
print("Last element:", my_tuple[-1])  # Output: 50

# accessing elements in a tuple using slicing
print("Elements from index 1 to 3:", my_tuple[1:4])  # Output: (20, 30, 40)

# concatenating two tuples
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
concatenated_tuple = tuple1 + tuple2
print("Concatenated tuple:", concatenated_tuple)  # Output: (1, 2, 3, 4, 5, 6)

# repeating a tuple
repeated_tuple = tuple1 * 3
print("Repeated tuple:", repeated_tuple)  # Output: (1, 2, 3, 1, 2, 3, 1, 2, 3)

# length of a tuple
print("Length of tuple1:", len(tuple1))  # Output: 3

# counting occurrences of an element in a tuple
count_tuple = (1, 2, 3, 1, 2, 1)
print("Count of 1 in count_tuple:", count_tuple.count(1))  # Output: 3

# finding the index of an element in a tuple
# returns the index of the first occurrence of the specified value
print("Index of 2 in count_tuple:", count_tuple.index(2))  # Output: 1

# sorted tuple
unsorted_tuple = (3, 1, 4, 2, 5)
sorted_tuple = tuple(sorted(unsorted_tuple))
print("Sorted tuple:", sorted_tuple)  # Output: (1, 2, 3, 4, 5)

# min() and max() functions
print("Minimum value in unsorted_tuple:", min(unsorted_tuple))  # Output: 1
print("Maximum value in unsorted_tuple:", max(unsorted_tuple))  # Output: 5

# cmp() function is not available in Python 3, but we can use comparison operators to 
# compare tuples
tuple_a = (1, 2, 3)
tuple_b = (1, 2, 3)
tuple_c = (1, 2, 4)

print("Comparing tuple_a and tuple_b:", tuple_a == tuple_b)  # Output: True
print("Comparing tuple_a and tuple_c:", tuple_a == tuple_c)  # Output: False

# tuple packing and unpacking
packed_tuple = 1, 2, 3, 4, 5  #packing the values into a tuple
print("Packed tuple:", packed_tuple)  # Output: (1, 2, 3, 4, 5)

# unpacking the tuple
a, b, c, d, e = packed_tuple
print("Unpacked values:", a, b, c, d, e)  # Output: 1 2 3 4 5


