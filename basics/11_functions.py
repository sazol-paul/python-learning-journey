#====================================
# Function
#====================================

'''A function is a block of code that performs a
specific task. Functions help in organizing code,
reusing code, and improving readability.'''

# syntax (example only - not executable)
# def function_name(parameters):
#     "Docstring"
#     # function body
#     return expression


#====================================
# Why Function
#====================================
num = 56
if num % 2 == 0:
    print(f"{num} is even.")
else:
    print(f"{num} is odd.")


def even_or_odd(num):
    """This function finds even or odd"""
    if num % 2 == 0:
        print(f"{num} is even.")
    else:
        print(f"{num} is odd.")

# Call the function
even_or_odd(6)


#====================================
# Function with multiple parameters
#====================================
def add(num1, num2):
    print(num1 + num2)

add(3, 4)


def mult(num3, num4):
    return num3 * num4

result = mult(4, 5)
print(result)


#====================================
# Default parameter
#====================================
def greet(name="Guest"):
    print(f"Hello, {name}")

greet()
greet("sazol")


#===================================
# Variable length argument
#===================================
# Positional argument (*args)
def print_num(*args):
    for number in args:
        print(number)

print_num(1, 2, 3, 4, 5, 6, "sazol")


# Keyword argument (**kwargs)
def print_details(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} : {value}")

print_details(name="sazol", age=20, country="Bangladesh")


# Both *args and **kwargs
def print_details(*args, **kwargs):
    for value in args:
        print(f"Positional Argument : {value}.")

    for key, value in kwargs.items():
        print(f"{key} : {value}")

print_details(1, 2, 3, 4, 5, 6, 7, "sazol",
              name="sazol", age=20, country="Bangladesh")