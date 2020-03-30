from nose.tools import eq_

from triangle import judge

def test_equilateral():
    eq_(1, judge(1, 1, 1))

def test_isosceles():
    eq_(2, judge(1, 1, 2))