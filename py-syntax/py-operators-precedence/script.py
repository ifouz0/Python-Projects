# The combination of values, variables, operators, and function calls is termed as an expression. 
# The Python interpreter can evaluate a valid expression. There can be more than one operator in an expression.
# To evaluate these types of expressions there is a rule of precedence in Python. 
# It guides the order in which these operations are carried out.

# For example, multiplication has higher precedence than subtraction.
# But we can change this order using parentheses () as it has higher precedence than multiplication.

# Multiplication has higher precedence than subtraction
print(10 - 4 * 2)

# Parentheses () has higher precedence
print((10 - 4) * 2)

# The operator precedence in Python is listed in the following table. 
# It is in descending order (upper group has higher precedence than the lower ones).
#
# Operators	                Meaning
# --------------------------------------------------------------------------
# ()	                    Parentheses
# **	                    Exponent
# +x, -x, ~x	            Unary plus, Unary minus, Bitwise NOT
# *, /, //, %	            Multiplication, Division, Floor division, Modulus
# +, -	                    Addition, Subtraction
# <<, >>	                Bitwise shift operators
# &	                        Bitwise AND
# ^	                        Bitwise XOR
# |	                        Bitwise OR
# ==, !=, >, >=, <, <=, 
# is, is not, in, not in	Comparisons, Identity, Membership operators
# not	                    Logical NOT
# and	                    Logical AND
# or	                    Logical OR

# We can see in the above table that more than one operator exists in the same group. These operators have the same precedence.
# When two operators have the same precedence, associativity helps to determine the order of operations.
# Associativity is the order in which an expression is evaluated that has multiple operators of the same precedence. 
# Almost all the operators have left-to-right associativity.

# For example, multiplication and floor division have the same precedence. 
# Hence, if both of them are present in an expression, the left one is evaluated first.

# Left-right associativity -> Output: 3
print(5 * 2 // 3)

# Shows left-right associativity -> Output: 0
print(5 * (2 // 3))

# Note: Exponent operator ** has right-to-left associativity in Python.
# We can see that 2 ** 3 ** 2 is equivalent to 2 ** (3 ** 2).

# Shows the right-left associativity of **
# Output: 512, Since 2**(3**2) = 2**9
print(2 ** 3 ** 2)

# If 2 needs to be exponated fisrt, need to use ()
# Output: 64
print((2 ** 3) ** 2)