# ============================================
# Palindrome Checker 
# ============================================

user_input = input("Enter a word or number: ")

user_input_lower = user_input.lower()

reversed_user_input = user_input_lower[::-1]

if user_input_lower == reversed_user_input:
  
    print(f"{user_input} is a palindrome.")
  
else:
  
    print(f"{user_input} isn't a palindrome.")