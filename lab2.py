from math import pi
from typing import NamedTuple

from geometry import Circle, Position


def full_name(first: str, mid: str, last: str) -> str:
    """Joins first, middle, and last names into a single string.

    >>> full_name('Harry', 'S', 'Truman')
    'Harry S Truman'
    >>> full_name('A', '', 'B')
    'A  B'
    """
    return first + mid + last


# We will write data definitions for a 3-D position,
# and then write functions for a Sphere data definition that uses the
# 3-D position.


class Position3(NamedTuple):
    """Represents a 3-D position.

    >>> Position3(0, 0, 0)
    Position3(x=0, y=0, z=0)
    >>> p = Position3(3, 4, 5.5)
    >>> p.x
    3
    >>> p.z
    5.5
    """
    x: float
    y: float
    z: float


class Sphere(NamedTuple):
    """Represents a sphere positioned on a 3-space.

    >>> c = Position3(1, 2, -3)
    >>> Sphere(c, 5)
    Sphere(center=Position3(x=1, y=2, z=-3), radius=5)
    """
    center: Position3
    radius: float


def sphere_volume(sphere: Sphere) -> float:
    """Computes the volume of a sphere."""
    return 4 * pi * ((sphere.radius ** 3) / 3)


def sphere_surface_area(sphere: Sphere) -> float:
    """Computes the surface area of a sphere."""
    return 4 * pi * (sphere.radius ** 2)


# Here we will define your own functions
# Please ask your Peer Mentors if you have any questions


def is_even(num: int) -> bool:
    """Determines whether the given `int` is even or odd.

    >>> is_even(3)
    False
    >>> is_even(4)
    True
    """
    return num%2 == 0


def deg_to_rad(deg: float) -> float:
    """Converts degrees to radians.

    >>> deg_to_rad(360) - 2 * pi
    0.0
    >>> deg_to_rad(90) - pi / 2
    0.0
    """
    pass # replace with your code


def circle_intersect(c1: Circle, c2: Circle) -> bool:
    """Determines whether two circles intersect."""
    pass # replace with your code


def sphere_intersect(s1: Sphere, s2: Sphere) -> float:
    """Determines whether two spheres intersect."""
    pass # replace with your code


def trilateration():
    """Given three spheres, finds the intersection
    points of the three spheres.
    """
    pass # replace with your code
