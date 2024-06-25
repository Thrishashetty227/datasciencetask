# Creating a list, dictionary, and set

# List
my_list = [2, 4, 3, 5, 4]
print("Original list:", my_list)

# Adding an element to the list
my_list.append(6)
print("List after adding an element:", my_list)

# Removing an element from the list
my_list.remove(3)
print("List after removing an element:", my_list)

# Modifying an element in the list
my_list[2] = 10
print("List after modifying an element:", my_list)

# Dictionary
my_dict = {'a': 3, 'b': 4, 'c': 5}
print("\nOriginal dictionary:", my_dict)

# Adding a key-value pair to the dictionary
my_dict['d'] = 6
print("Dictionary after adding a key-value pair:", my_dict)

# Removing a key-value pair from the dictionary
del my_dict['b']
print("Dictionary after removing a key-value pair:", my_dict)

# Modifying a value in the dictionary
my_dict['c'] = 1
print("Dictionary after modifying a value:", my_dict)

# Set
my_set = {1, 2, 3, 4, 5}
print("\nOriginal set:", my_set)

# Adding an element to the set
my_set.add(6)
print("Set after adding an element:", my_set)

# Removing an element from the set
my_set.remove(3)
print("Set after removing an element:", my_set)

# Sets do not support modifying elements directly, but you can remove and add elements
my_set.discard(4)  # remove element 4
my_set.add(10)  # add element 10
print("Set after modifying elements (removing and adding):", my_set)