"""
Python DocString: Documentación publica
-------------------------------------------
Module: script
"""

# Modules form Python Standard Library
import builtins  # Built-functions (no necesario)
import datetime
import math
import random

print("Welcome to Python", "!!")
print("Welcome to Python", "!!", sep = "####", end = "\n\n\n")
print('Welcome to Python', '!!', end = '.', sep = '####')
my_name = input("What is your name?")
print("Welcome to the course", my_name)  #Bad Smell!!
print("Welcome to the course" + my_name) #Bad Smell!!

print("PI: ", math.pi)
print("SQRT: ", math.sqrt(10))
print("CEIL: ", math.ceil(4.2))
print("CEIL: ", math.floor(4.2))



