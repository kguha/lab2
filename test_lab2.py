from lab2 import *
from math import pi
def test_calc_sphere():
    assert calc_sur_area(3) == 113.1

def test_str_len():
    assert str_len('Hello') == 5

def full_name():
    assert full_name('Abraham', None, 'Lincoln') == 'Abraham Lincoln'

def test_odd_or_even():
    assert is_even(2) == True

def test_deg_to_rad():
    assert deg_to_rad(360) == 2 * pi