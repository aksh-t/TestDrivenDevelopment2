from nose.tools import eq_

class Fibonacci:
    @classmethod
    def fib(cls, n):
        if n == 0:
            return 0
        if n == 1:
            return 1
        return cls.fib(n - 1) + cls.fib(n - 2)
    
def test_fibonacci():
    cases = [[0, 0], [1, 1], [2, 1], [3, 2]]
    for case in cases:
        eq_(case[1], Fibonacci.fib(case[0]))
