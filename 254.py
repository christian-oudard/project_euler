from utility import digits_of
from math import factorial
import itertools

def f(n):
    """
    >>> f(342)
    32
    """
    return sum(factorial(d) for d in digits_of(n))

def sf(n):
    """
    >>> sf(342)
    5
    """
    return sum(digits_of(f(n)))

def g(i):
    """
    >>> g(5)
    25
    >>> g(20)
    267
    >>> g(38)
    23599

    #>>> g(41)
    """
    for n in itertools.count(1):
        if sf(n) == i:
            return n

def sg(i):
    """
    >>> sg(5)
    7
    """
    return sum(digits_of(g(i)))

def sum_sg(limit):
    """
    >>> sum_sg(10)
    46
    >>> sum_sg(20)
    156
    >>> sum_sg(30)
    291
    """
    return sum(sg(i) for i in range(1, limit + 1))
