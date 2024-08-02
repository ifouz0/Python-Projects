b1 = True
b2 = False
#b3 = true       # NameError: name 'true' is not defined. Did you mean: 'True'?
#b4 = false      # NameError: name 'false' is not defined. Did you mean: 'False'?

print("-" * 50)

# ----------------------------------------------------------------
# Operator: and
# ----------------------------------------------------------------
# Syntax: x and y
# Description: Logical AND -> True if both the operands are true

print("Operator: and (Syntax: x and y)")
print("-" * 50)

op1 = True
op2 = True
result = op1 and op2
print(f"{op1} and {op2} = {result}")
#print("{} and {} = {}".format(op1, op2, result))
#print("{0} and {1} = {2}".format(op1, op2, result))
#print("{op1} and {op2} = {result}".format(op1 = op1, op2 = op2, result = result))


op1 = True
op2 = False
result = op1 and op2
print(f"{op1} and {op2} = {result}")

op1 = False
op2 = True
result = op1 and op2
print(f"{op1} and {op2} = {result}")

op1 = False
op2 = False
result = op1 and op2
print(f"{op1} and {op2} = {result}")

print("-" * 50)

# ----------------------------------------------------------------
# Operator: or
# ----------------------------------------------------------------
# Syntax: x or y
# Description: Logical OR -> True if either of the operands is true

print("Operator: or (Sintax: x or y)")
print("-" * 50)

op1 = True
op2 = True
result = op1 or op2
print(f"{op1} or {op2} = {result}")

op1 = True
op2 = False
result = op1 or op2
print(f"{op1} or {op2} = {result}")

op1 = False
op2 = True
result = op1 or op2
print(f"{op1} or {op2} = {result}")

op1 = False
op2 = False
result = op1 or op2
print(f"{op1} or {op2} = {result}")

print("-" * 50)

# ----------------------------------------------------------------
# Operator: not
# ----------------------------------------------------------------
# Syntax: not x
# Description: Logical NOT -> True if operand is false

print("Operator: not (Syntax: not x)")
print("-" * 50)

op1 = True
result = not op1
print(f"not {op1} : {result}")

op1 = False
result = not op1
print(f"not {op1} : {result}")

print("-" * 50)
