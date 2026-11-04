#=========================================
# Factorial Calculator
#=========================================

number = int(input("Enter a number: "))

if number < 0:
  
    print("Please select a positive number.")
  
elif number == 0:
  
    print("Your result is: 1")
  
else:
  
    factorial = 1
  
    for x in range(1, number + 1):
      
        factorial = factorial * x
      
    print(f"Your result is: {factorial}")