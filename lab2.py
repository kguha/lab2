#!/usr/bin/env python3
from math import isclose, pi

from geometry import *

from typing import NamedTuple


# Write a Python program to calculate surface volume and area of a sphere.
def calc_sphere():
    radian = float(input('Radius of sphere: '))
    sur_area = 4 * pi * radian ** 2
    volume = (4 / 3) * (pi * radian ** 3)
    print("Surface Area is: ", sur_area)
    print("Volume is: ", volume)

# Define a function that calculates the length of a string
def str_len():
    str = input("Please enter a string")
    length = len(str)
    return length


# Define a function that is your full name including first, middle
# and last name
def full_name():
    first = input("Enter your first name")
    mid = input("Enter your middle name")
    last = input("Enter your last name")
    full = first + mid + last
    return full

# Define a function that successfully tells you if your number is odd or even or divisible by your age


