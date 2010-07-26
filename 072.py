from fractions import Fraction
from utility import totient

def reduced_fractions(size):
    """
    >>> len(reduced_fractions(8))
    21
    """
    fractions = set()
    for d in range(2, size + 1):
        for n in range(1, d):
            fractions.add(Fraction(n, d))
    return fractions

def num_reduced_fractions(size):
    """
    >>> for i in range(40):
    ...     assert len(reduced_fractions(i)) == num_reduced_fractions(i)
    """
    return sum(totient(i) for i in range(2, size + 1))

print(num_reduced_fractions(1000000))
