# =================================================
# Declaring and Assigning Variables
# =================================================

name = "sazol"
age = 20
height = 5.7
is_student = True

print("Name:", name)
print("Age:", age)
print("Height:", height)
print("I am a student:", is_student)

# ==============================
# Naming Conventions
# ==============================

# 1. Variable names should be descriptive.
# 2. Must start with a letter or an underscore (_) and can contain letters, numbers, and underscores.
# 3. Variable names are case-sensitive.

# Valid variable names
first_name = "sazol"
last_name = "paul"

# Invalid variable names (commented out to prevent syntax errors):
# 2age = 20          # Cannot start with a number
# first-name = "sazol" # Cannot use hyphens
# @last_name = "paul"  # Cannot use special symbols

# ========================
# Case Sensitivity
# ========================
name = "sazol"
Name = "paul"

print("Is 'name' equal to 'Name'?:", name == Name)

# ================================================
# Understanding Variable Types
# ================================================

# Python is dynamically typed; the type of a variable is determined at runtime.

name = "sazol"
age = 20
height = 5.7
is_student = True

print(type(name))
print(type(age))
print(type(height))
print(type(is_student))

# =========================================
# Type Checking and Conversion
# =========================================

age = 20
print(type(age))

# Type conversion (Casting)
age_str = str(age)
print(type(age_str))

age_float = float(age)
print(type(age_float))

height = 5.7 
print(type(height))

height_int = int(height)
print(type(height_int))
print("Truncated height integer:", height_int)

# ================================
# Dynamic Typing
# ================================

# Python allows the type of a variable to change dynamically.

variable = 100
print(variable, type(variable))

variable = "sazol"
print(variable, type(variable))

variable = 34.9999
print(variable, type(variable))

# ==================================
# User Input
# ==================================

# input() returns a string by default
user_name = input("Enter your name: ")
print(f"Your name is: {user_name}")
