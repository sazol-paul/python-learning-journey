#======================================
# Simple calculator 
#======================================

num1 = float(input("Enter your first number: "))
num2 = float(input("Enter your second number: "))


operation = input("Enter your operation (+, -, *, /) ")
                  
if operation == "+":
    print(f"Your summation result is: {num1 + num2}")

elif operation == "-":
    print(f"Your subtraction result is: {num1 - num2}")
  
elif num2 == 0 and operation == "/":
    print("Error! Division by zero is not allowed.")
  
elif operation == "/":
    print(f"Your division result is: {num1 / num2}")
  
elif operation == "*":
    print(f"Your multiplication result is: {num1 * num2}")
  
else:
    print("Invalid operation selected.")
    
