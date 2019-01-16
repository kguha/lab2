from math import pi

from typing import NamedTuple

from geometry import *



def full_name(first: str, mid: str, last: str) -> str:
    # Define a function that is your full name including first, middle
    # and last name
    full = first + mid + last
    return full



#
# We will implement a Position and
# Sphere Tuple
#


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

#
# Here we will define your own functions
# Please ask your Peer Mentors if you have any questions
#


# Define a function that successfully tells you if your integer is odd or even or divisible by your age
# Return true if your number is even and
def is_even(num: int) -> bool:
    return


# Define a function to convert degrees to radian
def deg_to_rad(deg: float) -> float:
    return


# Define a function to calculate whether two circles intersect
def intersect(c1: Circle, c2: Circle) -> bool:
    return


# given a sphere of radius R located at (0, 0, 0) and
# a sphere or radius r located at (d, 0, 0)
# return the volume of the two spheres intersection
def overlap(s1: Sphere, s2: Sphere) -> float:
    return


# given three spheres, find the intersection
# points of the three spheres
def trilateration():
    return