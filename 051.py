from itertools import chain, combinations
from utility import is_prime, primes, digits_of, from_digits

def powerset(iterable):
    """
    >>> list(powerset([1,2,3]))
    [(), (1,), (2,), (3,), (1, 2), (1, 3), (2, 3), (1, 2, 3)]
    """
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s) + 1))

def position_combinations(n):
    """
    >>> list(position_combinations(2))
    []
    >>> list(position_combinations(29))
    [(0,)]
    >>> list(position_combinations(293))
    [(0,), (1,), (0, 1)]
    """
    length = len(digits_of(n))
    return filter(None, powerset(range(length - 1)))

def search(goal):
    """
    >>> search(6)
    13
    >>> search(7)
    56003
    """
    already_searched = set()
    for prime in primes():
        if prime in already_searched:
            continue
        positions_list = list(position_combinations(prime))
        for positions in positions_list:
            digits = list(digits_of(prime))
            family = set()
            for digit in range(10):
                if 0 in positions and digit == 0:
                    continue
                for pos in positions:
                    digits[pos] = digit
                number = from_digits(digits)
                if is_prime(number):
                    already_searched.add(number)
                    family.add(number)
            if len(family) >= goal:
                return min(family)

print(search(8))
