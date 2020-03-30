from nose.tools import eq_, raises

from triangle import judge, NonTriangleException

def test_equilateral():
    eq_(1, judge(1, 1, 1))

def test_isosceles():
    eq_(2, judge(2, 2, 1))
    eq_(2, judge(2, 1, 2))
    eq_(2, judge(1, 2, 2))

def test_scalene():
    eq_(3, judge(2, 3, 4))

@raises(NonTriangleException)
def test_non_triangle():
    judge(1, 1, 100)

@raises(NonTriangleException)
def test_all_zero_length():
    judge(0, 0, 0)

@raises(NonTriangleException)
def test_two_zero_length():
    judge(0, 0, 1)

@raises(NonTriangleException)
def test_one_zero_length():
    judge(0, 1, 1)