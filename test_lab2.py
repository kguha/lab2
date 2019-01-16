from math import isclose, pi

from lab2 import *


# This is what a failing test looks like.
def test_test():
    assert False == True, "Number is odd"


def test_full_name():
    actual = full_name('Abraham', 'The', 'Lincoln')
    expected = 'Abraham The Lincoln'
    assert actual == expected, 'this is not the lincoln'


def test_deg_to_rad():
    assert isclose(deg_to_rad(359.99999999999), 2 * pi)


def test_is_even():
    assert is_even(422) == True
