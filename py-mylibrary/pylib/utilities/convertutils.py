"""
Module Name: pylib.utilities.convertutils
Module Description: Conversion Utilities Module
"""
from math import pow, pi, floor
from pylib.utilities import mathutils


def bmi(weight: float, height: float) -> tuple[float,str,str]:
    """Python DocString"""
    bmi_index = weight / (pow(height, 2))
    bmi_category = "Undefined"

    if bmi_index < 18.5:
        bmi_category = "Underweight"
    elif 18.5 <= bmi_index < 25.0:
        bmi_category = "Normal weight"
    elif 25.0 <= bmi_index < 30.0:
        bmi_category = "Overweight"
    elif 30.0 <= bmi_index < 35.0:
        bmi_category = "Obesity class I"
    elif 35.0 <= bmi_index < 40.0:
        bmi_category = "Obesity class II"
    elif bmi_index >= 40.0:
        bmi_category = "Obesity class III"

    return (bmi_index, f"{bmi_index:.2f}", bmi_category)


def to_celsius(fahrenheit: float) -> float:
    """Python Docstring"""
    return 5/9 * (fahrenheit - 32)


def to_fahrenheit(celsius: float) -> float:
    """Python Docstring"""
    return 9/5 * celsius + 32


def to_radians(degrees: float) -> float:
    """Python Docstring"""
    return degrees * pi/180


def to_degrees(radians: float) -> float:
    """Python Docstring"""
    return radians * 180/pi


def seconds_to_dhm(seconds: int)-> tuple[int,int,int]:
    """Python Docstring"""
    (hours, minutes) = mathutils.modf(seconds/3600)
    return (hours // 24, hours % 24, floor(minutes * 60))


def degrees_to_dms(degrees: float) -> tuple[int,int,float]:
    '''Python DocString'''
    (degrees, rminutes) = mathutils.modf(degrees)
    (minutes, seconds) = mathutils.modf(rminutes * 60)

    return (degrees, minutes, seconds * 60)