# ====================================================
# Arithmetic Operations
# ====================================================

value1 = 20
value2 = 5

add_result = value1 + value2         # Addition
sub_result = value1 - value2         # Subtraction
mult_result = value1 * value2        # Multiplication
div_result = value1 / value2         # Division (float)
floor_div_result = value1 // value2  # Floor division (integer)
modulus_result = value1 % value2     # Modulus (remainder)
exponent_result = value1 ** value2   # Exponentiation (power)

print(f"Addition: {add_result}")
print(f"Subtraction: {sub_result}")
print(f"Multiplication: {mult_result}")
print(f"Division: {div_result}")
print(f"Floor Division: {floor_div_result}")
print(f"Modulus: {modulus_result}")
print(f"Exponentiation: {exponent_result}")

# =============================================
# Comparison Operators
# =============================================

# Equal to (==)
val1 = 20
val2 = 20
print("Equal numbers:", val1 == val2)

str1 = "sazol"
str2 = "sazol"
print("Equal strings:", str1 == str2)

str3 = "Sazol"
print("Case-sensitive equal:", str1 == str3)

# Not equal to (!=)
print("Not equal (case difference):", str1 != str3)

name1 = "sujoy"
name2 = "sujoy"
print("Not equal (identical strings):", name1 != name2)

# Greater than (>) and Less than (<)
num1 = 44
num2 = 55
print("Greater than:", num1 > num2)

num3 = 40
num4 = 50
print("Less than:", num3 < num4)

# Greater than or equal to (>=)
number1 = 10 
number2 = 10
print("Greater than or equal (equal):", number1 >= number2)

number3 = 40
number4 = 50
print("Greater than or equal (less):", number3 >= number4)

# Less than or equal to (<=)
number5 = 50
number6 = 40
print("Less than or equal (greater):", number5 <= number6)

number7 = 80
number8 = 80
print("Less than or equal (equal):", number7 <= number8)

# ============================================
# Logical Operators (and, or, not)
# ============================================

# and operator
x = True
y = True
z = False

print("True and True:", x and y)
print("True and False:", x and z)

# or operator
print("True or True:", x or y)
print("True or False:", x or z)

# not operator
print("not True:", not x)
print("not False:", not y)
