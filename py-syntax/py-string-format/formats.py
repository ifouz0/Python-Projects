import math
import random
import builtins

op1 = random.randint(a = 1, b = 100)
op2 = random.randint(1, 100)
op3 = random.randrange(start = 0, stop = 100, step = 2 )

rmax = max(op1, op2)
rmin = min(op1, op2)
rsqrt = math.sqrt(op3)

builtins.print("-" * 100)


print("MAX(", op1, ", ", op2, ") = ", rmax, sep = "")
print("MIN(", op1, ", ", op2, ") = ", rmin, sep = "")
print("SQRT(", op3, ") = ", rsqrt, sep = "")

print("-" * 100)

print("MAX(" + str(op1) +  ", " +  str(op2) + ") = " +  str(rmax))
print("MIN(" + str(op1) +  ", " +  str(op2) + ") = " +  str(rmin))
print("SQRT(" + str(op3) + ") = " + str(rsqrt))

print("-" * 100)

print("MAX(%d, %d = %d" % (op1, op2, rmax))
print("MIN(%d, %d = %d" % (op1, op2, rmin))
print("SQRT(%d) = %.2f" % (op3,rsqrt))

print("-" * 100)

print("MAX(%(p1)d, %(p2)d = %(p3)d" % {"p1": op1, "p2": op2, "p3": rmax})
print("MIN(%(p1)d, %(p2)d = %(p3)d" % {"p1": op1, "p2": op2, "p3": rmin})
print("SQRT(%(p1)d) = %(p2).2f" % {"p1": op3, "p2": rsqrt})

print("-" * 100)

print("MAX({}, {} = {}".format(op1, op2, rmax))
print("MIN({}, {} = {}".format(op1, op2, rmin))
print("SQRT({}) = {:.2f}".format(op3,rsqrt))

print("-" * 100)

print("MAX({0}, {1} = {2}".format(op1, op2, rmax))
print("MIN({0}, {1} = {2}".format(op1, op2, rmin))
print("SQRT({0}) = {1:.2f}".format(op3,rsqrt))

print("-" * 100)

print("MAX({p1}, {p2} = {p3}".format(p1 = op1, p2 = op2, p3 = rmax ))
print("MIN({p1}, {p2} = {p3}".format(p1 = op1, p2 = op2, p3 = rmin ))
print("SQRT({p1}) = {p2:.2f}".format(p1 = op3, p2 = rsqrt ))

print("-" * 100)

print(f"MAX({op1}, {op2} = {rmax}")
print(f"MIN({op1}, {op2} = {rmax}")
print(f"SQRT({op3}) = {rsqrt:.2f}")

print("-" * 100)

print(F"MAX({op1}, {op2} = {rmax}")
print(F"MIN({op1}, {op2} = {rmax}")
print(F"SQRT({op3}) = {rsqrt:.2f}")

print("-" * 100)

# “Old Style” String Formatting (% Operator)
# ---------------------------------------------------------------------
# Strings in Python have a unique built-in operation that can be accessed with the % operator. 
# This lets you do simple positional formatting very easily. If you’ve ever worked with a printf-style function in C, 
# you’ll recognize how this works instantly. Here’s a simple example:

print("For only %d dollars!" % 49)
print("For only %d dollars!" % (49))
print("My name is %s, I'm %d" % ("John", 36))
print("My name is %(fname)s, I'm %(age)d" % {"fname": "John", "age": 36})

# String Format Method
# ---------------------------------------------------------------------
# The format() method formats the specified value(s) and insert them inside the string's placeholder.
# The placeholder is defined using curly brackets: {}. Read more about the placeholders in the Placeholder section below.
# The format() method returns the formatted string.
#
# Syntax:  string.format(value1, value2...)
#
# The placeholders can be identified using named indexes {name}, numbered indexes {0}, or even empty placeholders {}.
#

print("For only {} dollars!".format(49))
print("For only {:.2f} dollars!".format(49))
print("For only {0:.2f} dollars!".format(49))
print("For only {price:.2f} dollars!".format(price = 49))

print("My name is {}, I'm {}".format("John", 36))
print("My name is {0}, I'm {1}".format("John", 36))
print("My name is {fname}, I'm {age}".format(fname = "John", age = 36))

# Formatting types:
# Inside the placeholders you can add a formatting type to format the result
# More info: https://www.w3schools.com/python/ref_string_format.asp

# String Interpolation (since Python 3.6+)
# ---------------------------------------------------------------------
# Python 3.6 added a new string formatting approach called formatted string literals or “f-strings”. 
# This new way of formatting strings lets you use embedded Python expressions inside string constants.

print(f"For only {49} dollars!")
print(f"For only {49:.2f} dollars!")
print(f"My name is {'John'}, I'm {36}")

print("hello" + "world")
print("hello" + str(2))