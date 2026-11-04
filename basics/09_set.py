#===============================
# set
#===============================

"""Sets are a built-in data type in Python used to
store collections of unique items. They are unordered, 
meaning that the elements do not follow a specific 
order, and they do not allow duplicate elements. 
Sets are useful for membership tests, eliminating 
duplicate entries, and performing mathematical set 
operations like union, intersection, difference, 
and symmetric difference."""

# Create a set
my_set = {1, 2, 3, 4, 5}
print(my_set)
print(type(my_set))

my_empty_set = set()
print(my_empty_set)

duplicate_set = {1, 1, 2, 2, 3, 4, 4, 5, 5}
print(duplicate_set)

my_set = set([1, 2, 3, 4, 5])
print(my_set)

number_set = set([1, 2, 3, 4, 5, 6, 7])
print(number_set)

#========================================
# Basics set operation 
#========================================

# Adding element
my_set.add(6)
print(my_set)

# Removing element
my_set.remove(5)
print(my_set)

#my_set.remove(8)
#print(my_set)

my_set.discard(2)
print(my_set)

my_set.discard(8)
print(my_set)

# Pop method 
my_set = {1, 2, 3, 4, 5, 6, 7, 8, 9}
removed_element = my_set.pop()
print(removed_element)

# Clear all the element
my_set.clear()
print(my_set)

# Set membership test 
my_set = {1, 2, 3, 4, 5, 6, 7, 8, 9}
print(2 in my_set)
print(10 in my_set)

# Mathematical operation
set1 = {1, 2, 3, 4, 5, 6}
set2 = {4, 5, 6, 7, 8, 9}

# union 
union_set = set1.union(set2)
print(union_set)

# Intersection 
intersection_set = set1.intersection(set2)
print(intersection_set)

set1.intersection_update(set2)
print(set1)

# Difference
set1 = {1, 2, 3, 4, 5, 6}
set2 = {4, 5, 6, 7, 8, 9}

print(set1.difference(set2))
print(set2.difference(set1))

# Symmetric difference
print(set1.symmetric_difference(set2))

# Sets method
set1 = {1, 2, 3, 4, 5}
set2 = {3, 4, 5}

# Issubset method
print(set1.issubset(set2))
print(set2.issubset(set1))

# Issuperset method
print(set1.issuperset(set2))
print(set2.issuperset(set1))
