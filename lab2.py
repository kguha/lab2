from math import pi

from typing import NamedTuple


# Write a Python program to calculate surface volume and surface area of a sphere.
def calc_sur_area(radius :float):
    sur_area = 4 * pi * radius ** 2
    return sur_area

# Define a function that calculates the length of a string
def str_len(string: str):
    print("Type your code here")
    return string


# Define a function that is your full name including first, middle
# and last name
def full_name(first: str, mid: str, last: str):
    full = first + mid + last
    return full

# Define a function that successfully tells you if your number is odd or even or divisible by your age
def odd_or_even(num: int):
    return

# Define a function to convert degree to radian.
def deg_to_rad(deg: float):
    return

def calc_vol(radius: float):
    return

class Sphere(NamedTuple):
    """Represents a sphere positioned on a 3-D plane."""
    radius: float = 0

    # please define your volume function
    def volume(self) -> float:
        return calc_vol(self.radius)

    def surface_area(self) -> float:
        return calc_sur_area(self.radius)