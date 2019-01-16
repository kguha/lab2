from lab2 import *
from math import isclose, pi


def test_is_even():
    assert False == True,"Number is odd"


def test_full_name():
    assert full_name('Abraham', 'The', 'Lincoln') == 'AbrahamTheLincoln','this is not the lincoln'


def test_deg_to_rad():
    r = deg_to_rad(359.99999)
    assert isclose(deg_to_rad(r), 2 * pi)


def test_is_even():
    assert is_even(422) == True