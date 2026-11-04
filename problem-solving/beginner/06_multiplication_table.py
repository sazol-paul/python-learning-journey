#=========================================
# Multiplication Table Generator
#========================================

try:
  
    number = int(input("Enter a number: "))
  
except ValueError:
  
    print("Please enter a valid integer.")
  
else:
  
    for num in range(1, 11):
      
        print(f"{num} x {number} = {num * number}")