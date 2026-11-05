#=========================================
# Dictionaries
#=========================================

"""
Dictionaries are unordered collections of items.
They store data in key-value pairs. Keys must be unique
and immutable (e.g., strings, numbers, or tuples), while
values can be of any type.
"""

#======================================
# Creating Dictionaries
#======================================
empty_dict = {}
print(type(empty_dict))

empty_dict = dict()
print(type(empty_dict))

info_dict = {"name": "sazol", "age": 20, "grade": 21}
print(info_dict)

# A single key is always used (last value wins)
info_dict = {"name": "sazol", "age": 20, "name": "adam"}
print(info_dict)   # {'name': 'adam', 'age': 20}

#======================================
# Accessing Dictionary Elements
#======================================
student = {"name": "sazol", "age": 20, "grade": "A"}
print(student["age"])
print(student["grade"])

# Accessing using get() method
print(student.get("name"))
print(student.get("last_name"))                    # None
print(student.get("last_name", "Not available"))   # default value

#======================================
# Modifying Dictionary Elements
#======================================
# Dictionaries are mutable, so you can add, update or delete elements
student = {"name": "sazol", "age": 20, "grade": "A"}
print(student)

# Update value for the key
student["age"] = 18
print(student)

# Add a new key and value
student["address"] = "Bangladesh"
print(student)

# Delete key and value pair
del student["grade"]
print(student)

#======================================
# Dictionary Methods
#======================================
# Get all the keys
keys = student.keys()
print(keys)
print(list(keys))       # convert to list if needed

# Get all the values
values = student.values()
print(values)

# Get all key-value pairs
items = student.items()
print(items)

#=========================================
# Reference Copy vs Shallow Copy
#=========================================
# Reference copy (alias) — both variables point to the SAME object
student_copy = student
print(student)
print(student_copy)

student["name"] = "harry"
print(student)
print(student_copy)     # changes reflect here too (same object)

# Shallow copy — creates a NEW object with same values
student_copy1 = student.copy()
print(student_copy1)
print(student)

student["name"] = "danny"
print(student_copy1)    # unchanged (different object)
print(student)

#=========================================
# Iterating Over Dictionaries
#=========================================
# You can use loops to iterate over keys, values or items

# Iterating over keys
for key in student.keys():
    print(key)

# Iterating over values
for value in student.values():
    print(value)

# Iterating over items
for key, value in student.items():
    print(f"{key} : {value}")

#=========================================
# Nested Dictionaries
#=========================================
students = {
    "student1": {"name": "sazol", "age": 20},
    "student2": {"name": "harry", "age": 21}
}
print(students)

# Accessing nested dictionary elements
print(students["student1"]["name"])
print(students["student2"]["age"])

# Iterating through nested dictionaries
for student_id, student_info in students.items():
    print(f"{student_id} : {student_info}")
    for key, value in student_info.items():
        print(f"{key} : {value}")

#=========================================
# Dictionary Comprehension
#=========================================
squares = {i: i ** 2 for i in range(1, 6)}
print(squares)

# Conditional dictionary comprehension
evens = {x: x ** 2 for x in range(1, 11) if x % 2 == 0}
print(evens)