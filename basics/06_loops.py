# ===============================================
# For loop
# ===============================================

for i in range(0, 6):
    print(i)

for i in range(1, 6):
    print(i)

for i in range(1, 11, 2):
    print(i)

for i in range(10, 1, -1):
    print(i)

for i in range(10, 1, -2):
    print(i)

# String
full_name = "sazol paul"

for i in full_name:
    print(i)

# ==================================
# While loop
# ==================================

# The while loop continues to execute as long as the condition is true.
count = 0

while count < 5:
    print(count)
    count = count + 1

# ============================================
# Loop control statements
# ============================================

# ==============================================
# Break statement
# ==============================================

# The break statement exits the loop prematurely.
for i in range(11):
    if i == 5:
        break
    print(i)

# ==========================================
# Continue statement
# ==========================================

# The continue statement skips the current iteration and continues with the next.
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)

# =============================================
# Pass statement
# =============================================

# The pass statement is a null operation; it does nothing.
for i in range(5):
    if i == 3:
        pass
    print(i)

# =============================================
# Nested loops
# =============================================

# A loop inside a loop
for i in range(1, 3):
    for j in range(1, 5):
        print(f"i : {i} and j : {j}")
