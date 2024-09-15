from functools import reduce

def factorial(n):
    """Factorial implemented with reduce and anonymous function"""
    return reduce(lambda a, b: a*b, range(1, n+1))

from functools import reduce
from operator import mul

def factorial_new(n):
    """Factorial implemented with reduce and operator.mul"""
    return reduce(mul, range(1, n+1))