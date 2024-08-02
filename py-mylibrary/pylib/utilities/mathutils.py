"""
Module Name: pylib.utilities.mathutils
Module Description: Math Utilities Module
"""
import math

# Atributos o variables a nivel de módulo
PI:float = 3.14159265358979323846
E:float = 2.718281828459045235360
PHI:float = (1 + math.sqrt(5)) / 2
BASE_BINARY:int = 2
BASE_OCTAL:int = 8
BASE_DECIMAL:int = 10
BASE_HEXADECIMAL:int = 16


# Funciones o métodos a nivel de módulo (Helpers / Utilities Functions)
def abs(value:int|float) -> int|float:
    """Python DocString"""
    return value if value >= 0 else -value


def is_even(value:int) -> bool:
    """Python DocString"""
    return value % 2 == 0


def is_odd(value:int) -> bool:
    """Python DocString"""
    return not is_even(value)


def is_prime(value:int) -> bool:
    """Python DocString"""
    for num in range(value - 1, 1, -1):
        if value % num == 0: 
            return False
    return True   

def factorial(value:int) -> int:
    """Python DocString"""
    if value == 1: return 1
    return value * factorial(value = value - 1)


def max(op1: int|float, op2: int|float, *ops: int|float) -> int|float:
    '''Python DocString'''
    rmax = op1 if op1 >= op2 else op2
    for op in  ops:
        rmax = op if op >= rmax else rmax
    return rmax


def min(op1: int|float, op2: int|float, *ops: int|float) -> int|float:
    '''Python DocString'''
    rmin = op1 if op1 <= op2 else op2
    for op in  ops:
        rmin = op if op <= rmin else rmin
    return rmin


def sum(op1: int|float, op2: int|float, *ops: int|float) -> int|float:
    '''Python DocString'''
    rsum = op1 + op2
    for op in ops:
        rsum += op
    return rsum


def average(op1: int|float, op2: int|float, *ops: int|float) -> int|float:
    '''Python DocString'''
    return sum(op1,op2,*ops)/(len(ops) + 2)


def modf(value: float) -> tuple[int,float]:
    '''Python DocString'''
    return (int(value), abs(int(value) - value))

