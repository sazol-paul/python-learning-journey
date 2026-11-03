#=================================================
# Tuple 
#=================================================

# A tuple is an ordered and immutable collection of elements.

# Creating a tuple
empty_tuple = ()
print(empty_tuple, type(empty_tuple))

lst = list()
print(type(lst))

tpl = tuple()
print(type(tpl))

numbers = tuple([1, 2, 3, 4, 5, 6, 7])
print(numbers)
print(type(numbers))

num_tuple = (1, 2, 3, 4, 5, 6)
print(type(num_tuple))
print(num_tuple)

mixed_tuple = (1, 2, 3, "hello world", True)
print(type(mixed_tuple))
print(mixed_tuple)

# Accessing tuple elements
print(numbers[2])
print(numbers[-1])
print(numbers[1:5])
print(numbers[:5])
print(numbers[::2])
print(numbers[::-1])
print(numbers[::-2])

# Tuple operation 
concatenation_tuple = numbers + mixed_tuple
print(concatenation_tuple)

print(mixed_tuple * 3)
print(numbers * 3)

# Immutable nature of tuple
#numbers[1] = "sazol"
#print(numbers)

# Tuple methods
print(numbers.count(5))
print(numbers.index(3))

# Packing and unpacking tuple
# Packing
packed_tuple = 1, "hello world", 3.14, True
print(packed_tuple)

# unpacking
a, b, c, d = packed_tuple
print(a)
print(b)
print(c)
print(d)

# Unpacking with *
numbers = (1, 2, 3, 4, 5, 6, 7)
first, *middle, last = numbers
print(first)
print(middle)
print(last)

*first, middle, last = numbers
print(first)
print(middle)
print(last)

first, middle, *last = numbers
print(first)
print(middle)
print(last)

#========================================
# Nested tuple
#========================================
# Nested list
lst = [[1, "sazol", 3.14, "a"], [1, 2, 3, 4], [5, 6, 7, 8]]

print(lst[2][0:2])
print(lst[0][0:3])

# Nested tuple
nested_tuple = (("sazol", 1, 3.14, "b"), (2, 3, "hello world", "v"), (4, 5, 6, 7))
print(nested_tuple[0])
print(nested_tuple[2][1:3])

# Iterating over nested tuple
for sub_tuple in nested_tuple:
  
    for item in sub_tuple:
      
        print(item, end=" ")

    print()
    