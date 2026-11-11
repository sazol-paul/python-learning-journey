
# ============================================
# Lambda Functions
# ============================================

"""
Lambda functions are anonymous functions
that can have multiple arguments but only
one expression.
"""

# Normal Function
def addition(num1, num2):
    return num1 + num2

print(addition(2, 3))


# Lambda Function
add = lambda num1, num2: num1 + num2

print(add(6, 7))


# ============================================
# Even Number
# ============================================

# Normal Function
def is_even(num):
    return num % 2 == 0

print(is_even(44))


# Lambda Function
even = lambda num: num % 2 == 0

print(even(6))


# ============================================
# Three Numbers Addition
# ============================================

# Normal Function
def add_three(num1, num2, num3):
    return num1 + num2 + num3

print(add_three(3, 4, 5))


# Lambda Function
add_three_lambda = lambda num1, num2, num3: num1 + num2 + num3

print(add_three_lambda(22, 33, 44))
