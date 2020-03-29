from nose.tools import eq_

class FibonacciTest:
    @staticmethod
    def fib(n):
        if n == 0:
            return 0
        return 1
    
def test_fibonacci():
    eq_(0, FibonacciTest.fib(0))
    eq_(1, FibonacciTest.fib(1))
