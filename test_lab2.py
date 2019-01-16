from lab2 import *
from math import isclose, pi


def test_is_even():
    assert False == True, "Number is odd"


def test_full_name():
    actual = full_name('Abraham', 'The', 'Lincoln')
    expected = 'AbrahamTheLincoln'
    assert actual == expected, 'this is not the lincoln'


def test_deg_to_rad():
    r = deg_to_rad(359.99999)
    assert isclose(deg_to_rad(r), 2 * pi)


def test_is_even_again():
    assert is_even(422) == True
