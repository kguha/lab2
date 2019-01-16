from math import pi

from typing import NamedTuple

from geometry import *


def full_name(first: str, mid: str, last: str) -> str:
    """Define a function that is your full name including first, middle
    and last name
    """
    full = first + mid + last
    return full



"""""
We will implement a Position and
Sphere Tuple
"""

class Position(NamedTuple):
    # Represents a 3-D position.
    x: float


class Sphere(NamedTuple):
    """
    Represents a sphere positioned on a 3-space.
    """
    center: Position
    radius: float

    # please define volume of a sphere
    def volume(self) -> float:
        # your code goes here
        return

    # please define surface area of a sphere
    def surface_area(self) -> float:
        # your code goes here
        return

"""
Here we will define your own functions
Please ask your Peer Mentors if you have any questions
"""



def is_even(num: int) -> bool:
    """Define a function that successfully tells you if your integer is
    odd or even or divisible by your age
    Return true if your number is even and
    """
    return False


def deg_to_rad(deg: float) -> float:
    # Define a function to convert degrees to radian
    return


def intersect(c1: Circle, c2: Circle) -> bool:
    # Define a function to calculate whether two circles intersect
    return


def overlap(s1: Sphere, s2: Sphere) -> float:
    """given a sphere of radius R located at (0, 0, 0) and
    a sphere or radius r located at (d, 0, 0)
    return the volume of the two spheres intersection
    """
    return


def trilateration():
    """given three spheres, find the intersection
    points of the three spheres
    """
    return
