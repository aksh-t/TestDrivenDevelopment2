from nose.tools import eq_

class FibonacciTest:
    @staticmethod
    def fib(n):
        if n == 0:
            return 0
        return 1
    
def test_fibonacci():
    cases = [[0, 0], [1, 1]]
    for case in cases:
        eq_(case[1], FibonacciTest.fib(case[0]))
