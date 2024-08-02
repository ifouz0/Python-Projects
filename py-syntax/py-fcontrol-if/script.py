# ----------------------------------------------------------------
# Flow Control: The if statement
# ----------------------------------------------------------------
# Syntax: 
# 
# if condition:
#   statement(s)
#

# If the number is positive, we print an appropriate message
num = 3
if num > 0:
    print(f"{num} is a positive number.")

print("This is always printed.")

num = -1
if num > 0:
    print(f"{num} is a positive number.")

print("This is also always printed.")


# ----------------------------------------------------------------
# Flow Control: The if..else statement
# ----------------------------------------------------------------
# Syntax: 
# 
# if condition:
#   statement(s)
# else:
#   statements(s)
#

# Program checks if the number is positive or negative
# And displays an appropriate message
num = 3
if num >= 0:
    print(f"{num} is a positive number or zero")
else:
    print(f"{num} is a negative number")


# ----------------------------------------------------------------
# Flow Control: The if..elif..else statement
# ----------------------------------------------------------------
# Syntax: 
# 
# if condition:
#   statement(s)
# elif condition:
#   statements(s)
# else:
#   statements(s)
#

num = 3.4
if num > 0:
    print(f"{num} is a positive number")
elif num == 0:
    print(f"{num} is Zero")
else:
    print(f"{num} is a negative number")


# ----------------------------------------------------------------
# Flow Control: Conditional Expressions
# ----------------------------------------------------------------
# Syntax: 
# 
# result_if_true if condition else result_if_false
# (result_if_false, result_if_true)[condition]

num = 4
result = True if num % 2 == 0 else False
print(result)
result = (False,True)[num % 2 == 0]
print(result)

