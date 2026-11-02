#================================
# List
#================================

lst = []
print(type(lst))

names = ["sazol", "sujoy", "puza", 1, 2, 3, 4, 5]
print(names)

mixed_list = [1, "sazol", 3.14, True]
print(mixed_list)

# Accessing list element
fruits = ["apple", "banana", "cherry", "jackfruit", "watermelon", "kiwi"]
print(fruits[0])
print(fruits[3])
print(fruits[5])
print(fruits[-1])
print(fruits[1:])
print(fruits[1:4])
print(fruits[-1:])

# Modifying the list elements
fruits[1] = "lemon"
print(fruits)

fruits = ["apple", "banana", "cherry", "jackfruit", "watermelon", "kiwi"]

# List methods
fruits.append("orange") # Add an item to the end 
print(fruits)

fruits.insert(1, "guava")
print(fruits)

fruits.remove("banana") # Remove the first occurrence of an item
print(fruits)

# Remove and return the last element
popped_fruits = fruits.pop()
print(popped_fruits)
print(fruits)

index = fruits.index("watermelon")
print(index)

fruits = ["apple", "banana", "cherry", "jackfruit", "watermelon", "kiwi"]
fruits.insert(2, "banana")
print(fruits)
print(fruits.count("banana"))

fruits.sort() # Sort the list in ascending order
print(fruits)

fruits.reverse() # Reverse the list 
print(fruits)

fruits.clear() # Remove all items from the list
print(fruits)

#================================================
# Slicing list
#================================================

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(numbers[1:5])
print(numbers[:5])
print(numbers[::2])
print(numbers[::-1])
print(numbers[::-2])

#================================================
# Iterating over list
#================================================

fruits = ["apple", "banana", "cherry", "jackfruit", "watermelon", "kiwi"]

for fruit in fruits:
    print(fruit)

#============================================
# Iterating with index 
#============================================

for index, fruit in enumerate(fruits):
    print(index, fruit)

#============================================
# List comprehension
#============================================
lst = []
for x in range(1, 11):
    lst.append(x ** 2)

print(lst)


#=================================================
# Basic list comprehension
#=================================================

square = [x ** 2 for x in range(1, 11)]
print(square)

# List comprehension with condition
lst = []
for i in range(1, 11):
    if i % 2 == 0:
        lst.append(i)

print(lst)  

even_numbers = [num for num in range(1, 17) if num % 2 == 0]
print(even_numbers)

#================================================
# Nested list comprehension
#================================================

lst1 = [1, 2, 3, 4]
lst2 = ["a", "b", "c", "d"]

pair = [[i, j] for i in lst1 for j in lst2]
print(pair)

# List comprehension with function calls

words = ["hello", "world", "python", "list", "comprehension"]
lengths = [len(word) for word in words]
print(lengths)