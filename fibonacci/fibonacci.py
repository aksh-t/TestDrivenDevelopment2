from nose.tools import eq_

class FibonacciTest:
    @staticmethod
    def fib(n):
        return 0
    
def test_fibonacci():
    eq_(0, FibonacciTest.fib(0))
