from math import pi

from typing import NamedTuple




def full_name(first: str, mid: str, last: str):
    # Define a function that is your full name including first, middle
    # and last name
    full = first + mid + last
    return full



def str_len(string: str):
    # Define a function that calculates the length of a string
    print("Type your code here")
    return string




def is_even(num: int):
    # Define a function that successfully tells you if your number is odd or even or divisible by your age
    # Return true if your number is even and
    return



def deg_to_rad(deg: float):
    # Define a function to convert degree to radian.
    return


def calc_vol(radius: float):
    return


class Position(NamedTuple):
    # Represents a 3-D position.
    x: float
    y: float
    z: float
    # Put the rest of your code here
    #


class Sphere(NamedTuple):
    # Represents a sphere positioned on a 3-space.
    center: Position
    radius: float

    # please define volume of a sphere
    def volume(self) -> float:
        # your code goes here
        return  (4/3) * pi * self.radius ** 3

    # please define surface area of a sphere
    def surface_area(self) -> float:
        # your code goes here
        return 4 * pi * self.radius ** 2


def overlap(s1: Sphere, s2: Sphere):
    # given a sphere of radius R located at (0, 0, 0) and
    # a sphere or radius r located at (d, 0, 0)
    # return the volume of the two spheres intersection
    return

def tangent(blah):
    return