#=========================================
# If statement
#=========================================

age = 18 

if age >= 18:
  print("You are allowed to vote in the elections")


#=========================================
# Else statement
#=========================================

# The else statement executes a block of code if the condition  in the if statement is false.
age = 17

if age >= 18:
  print("You are allowed to vote in the elections")
else:
  print("You are not allowed to vote in the elections")

#==============================================
# Elif statement
#==============================================

# The elif statement allows you to check multiple conditions. It stands for "else if"
age = 10

if age < 13:
  print("You are a child")
elif age < 18:
  print("You are a teenager")
else:
  print("You are an adult")

#================================================
# Nested conditional statement
#================================================

# You can place one or more if, elif or else statement inside another if, elif, else statement to create nested conditional statements.
number = int(input("Enter the number : "))

if number > 0:
  print("The number is positive")
  if number % 2 == 0:
    print("The number is even")
  else:
    print("The number is odd")

else:
  print("The number is zero or negative")

  
