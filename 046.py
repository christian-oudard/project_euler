from utility import is_prime, up_to, primes, isqrt, is_perfect_square
from itertools import count, islice

def odd_composites():
    """
    >>> list(up_to(33, odd_composites()))
    [9, 15, 21, 25, 27, 33]
    """
    for odd in islice(count(3), None, None, 2):
        if not is_prime(odd):
            yield odd

def decompose_prime_square(n):
    """
    Attempt to write n as the sum of a prime and twice a square.

    >>> decompose_prime_square(9)
    (7, 1)
    >>> decompose_prime_square(15)
    (7, 2)
    >>> decompose_prime_square(21)
    (3, 3)
    >>> decompose_prime_square(25)
    (7, 3)
    >>> decompose_prime_square(27)
    (19, 2)
    >>> decompose_prime_square(33)
    (31, 1)
    """
    for p in up_to(n, primes()):
        if p == 2:
            continue
        residue = n - p
        assert residue % 2 == 0, residue
        square = residue // 2
        if is_perfect_square(square):
            return (p, isqrt(square))

for n in odd_composites():
    if decompose_prime_square(n) is None:
        print(n)
        break
