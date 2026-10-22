# create a empty set
empty_set = set()
print("Empty set:", empty_set)  # Output: Empty set: set()

# create a set using list
list = [1, 2, 3, 4, 5, 1, 2, 3]
set_from_list = set(list)
print("Set from list:", set_from_list)  # Output: Set from list: {1, 2, 3, 4, 5}

# adding elements to a set
my_set = {1, 2, 3}
my_set.add(4)
print("Set after adding an element:", my_set)  # Output: Set after adding an element: {1, 2, 3, 4}

# Updating a set with multiple elements
my_set.update([5, 6, 7])
print("Set after updating with multiple elements:", my_set)  
# Output: Set after updating with multiple elements: {1, 2, 3, 4, 5, 6, 7}

# copying a set
copied_set = my_set.copy()
print("Copied set:", copied_set)  # Output: Copied set: {1, 2, 3, 4, 5, 6, 7}

# popping an element from a set
popped_element = my_set.pop()
print("Popped element:", popped_element) 
# Output: Popped element: (random element from the set)
print("Set after popping an element:", my_set)
# Output: Set after popping an element: (remaining elements in the set)

# removing an element from a set
my_set.remove(2)
print("Set after removing an element:", my_set) 
# Output: Set after removing an element: {1, 3, 4, 5, 6, 7}


#discarding an element from a set
my_set.discard(3)
print("Set after discarding an element:", my_set)
# Output: Set after discarding an element: {1, 4, 5, 6, 7}
# if the element is not present, discard() will not raise an error

# clearing a set
my_set.clear()
print("Set after clearing:", my_set)  # Output: Set after clearing: set()

# union of two sets
set1 = {1, 2, 3}
set2 = {3, 4, 5}
union_set = set1.union(set2)
print("Union of set1 and set2:", union_set)  # Output: Union of set1 and set2: {1, 2, 3, 4, 5}

# intersection of two sets
intersection_set = set1.intersection(set2)
print("Intersection of set1 and set2:", intersection_set)
# Output: Intersection of set1 and set2: {3}
print("Intersection of set1 and set2:", set1 & set2)
# Output: Intersection of set1 and set2: {3}

# difference of two sets
# difference returns a set containing elements that are in the first set but not in the second set
difference_set = set1.difference(set2)
print("Difference of set1 and set2:", difference_set)
print("Difference of set1 and set2:", set1 - set2)
# Output: Difference of set1 and set2: {1, 2}

# symmetric difference of two sets
# symmetric difference returns a set containing elements that are in either of the sets
# but not in both
# create a set with unique elements from both sets
symmetric_difference_set = set1.symmetric_difference(set2)
print("Symmetric difference of set1 and set2:", symmetric_difference_set)
# Output: Symmetric difference of set1 and set2: {1, 2, 4, 5}


