#! /usr/bin/python3

import math
import time
import itertools
import random
from copy import copy
from collections import defaultdict

_n = 2 # the current number being considered as a prime
_composites = {} # a mapping from composite numbers to the smallest prime that is a factor of it (its witness)
_primes = [] # primes found so far
def primes():
    global _n, _composites, _primes
    for p in _primes:
        yield p
    while True:
        if _n not in _composites:
            # not a composite, therefore prime
            _primes.append(_n)
            yield _n
            _composites[_n**2] = _n # the next unseen composite number here will be n squared
        else: # n is a composite number
            # find the next unseen composite number with the same witness as n
            witness = _composites.pop(_n)
            next = _n + witness
            while next in _composites:
                next += witness
            _composites[next] = witness
        _n += 1

def prime_factorization(n):
    """
    Return the prime factors of n, as a list, including repeats.

    >>> prime_factorization(1)
    []
    >>> prime_factorization(2)
    [2]
    >>> prime_factorization(4)
    [2, 2]
    >>> prime_factorization(8)
    [2, 2, 2]
    >>> prime_factorization(12)
    [2, 2, 3]
    >>> prime_factorization(600851475143)
    [71, 839, 1471, 6857]
    """
    factors = []
    while True:
        for p in up_to(math.ceil(math.sqrt(n)), primes()):
            quotient, remainder = divmod(n, p)
            if remainder == 0:
                factors.append(p)
                n = quotient
                break
        else:
            if n != 1:
                factors.append(n)
            return factors

def is_prime(n):
    if n < 2:
        return False
    for i in up_to_sqrt_of(n):
        if n % i == 0:
            return False
    return True

_mrpt_num_trials = 5
def is_probable_prime(n):
    """
    Miller-Rabin primality test.
    
    A return value of False means n is certainly not prime. A return value of
    True means n is very likely a prime.
    
    >>> is_probable_prime(2)
    True
    >>> is_probable_prime(3)
    True
    >>> is_probable_prime(4)
    False
    >>> is_probable_prime(5)
    True
    >>> is_probable_prime(123456789)
    False
    >>> is_probable_prime(6438080068035544392301298549614926991513861075340134\
3291807343952413826484237063006136971539473913409092293733259038472039\
7133335969549256322620979036686633213903952966175107096769180017646161\
851573147596390153)
    True
    >>> is_probable_prime(7438080068035544392301298549614926991513861075340134\
3291807343952413826484237063006136971539473913409092293733259038472039\
7133335969549256322620979036686633213903952966175107096769180017646161\
851573147596390153)
    False
    """
    # special case 2
    if n == 2:
        return True
    # ensure n is odd
    if n % 2 == 0:
        return False
    # write n-1 as 2**s * d
    # repeatedly try to divide n-1 by 2
    s = 0
    d = n-1
    while True:
        quotient, remainder = divmod(d, 2)
        if remainder == 1:
            break
        s += 1
        d = quotient
    assert(2**s * d == n-1)

    # test whether a is a witness for the compositeness of n
    def try_composite(a):
        if pow(a, d, n) == 1:
            return False
        for i in range(s):
            if pow(a, 2**i * d, n) == n-1:
                return False
        return True # n is definitely composite

    for i in range(_mrpt_num_trials):
        a = random.randint(2, n-1) 
        if try_composite(a):
            return False

    return True # no trial number showed n as composite

def totient(n):
    """
    Euler's totient function.

    >>> [totient(n) for n in range(1, 70)]
    [1, 1, 2, 2, 4, 2, 6, 4, 6, 4, 10, 4, 12, 6, 8, 8, 16, 6, 18, 8, 12, 10, 22, 8, 20, 12, 18, 12, 28, 8, 30, 16, 20, 16, 24, 12, 36, 18, 24, 16, 40, 12, 42, 20, 24, 22, 46, 16, 42, 20, 32, 24, 52, 18, 40, 24, 36, 28, 58, 16, 60, 30, 36, 32, 48, 20, 66, 32, 44]
    """
    totient = n
    for p in set(prime_factorization(n)):
        totient -= totient // p
    return totient

def gcd(a, b):
    """
    Euclid's algorithm to find the greatest common denominator.

    >>> gcd(12, 21)
    3
    >>> gcd(53473753604, 32407556409)
    271
    """
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    """
    Least common multiple.

    >>> lcm(21, 6)
    42
    """
    return a * b // gcd(a, b)

def up_to(n, iterable):
    return list(itertools.takewhile(lambda i: i <= n, iterable))

def up_to_sqrt_of(n):
    """
    >>> max(up_to_sqrt_of(196))
    14
    """
    return range(2, math.floor(math.sqrt(n)) + 1)

def product(iterable):
    prod = 1
    for n in iterable:
        prod *= n
    return prod

def nth(iterable, n):
    """Get the Nth item in the iterable."""
    return list(itertools.islice(iterable, n, n+1))[0]

def all_pairs(iterable):
    enumerated_values = list(enumerate(iterable))
    for low_index, first_item in enumerated_values:
        for high_index, second_item in enumerated_values[low_index + 1:]:
            yield (first_item, second_item)

def frequency_count(l):
    """
    >>> frequency_count('aaabbc') == {'a': 3, 'b': 2, 'c': 1}
    True
    """
    frequencies = defaultdict(int)
    for i in l:
        frequencies[i] += 1
    return dict(frequencies)

def num_divisors(n):
    """
    >>> num_divisors(12)
    6
    >>> num_divisors(28)
    6
    """
    pf = prime_factorization(n)
    fc = frequency_count(pf).values()
    return product(f + 1 for f in fc)

def proper_divisors(n):
    """
    >>> proper_divisors(12)
    [1, 2, 3, 4, 6]
    >>> proper_divisors(28)
    [1, 2, 4, 7, 14]
    >>> proper_divisors(0)
    []
    >>> proper_divisors(1)
    []
    >>> proper_divisors(196)
    [1, 2, 4, 7, 14, 28, 49, 98]
    """
    if n < 2:
        return []
    divisors = {1}
    for i in up_to_sqrt_of(n):
        if n % i == 0:
            divisors.add(i)
            divisors.add(n//i)
    return sorted(list(divisors))

def all_combinations(sequence):
    """
    >>> list(all_combinations('ab'))
    [(), ('a',), ('b',), ('a', 'b')]
    """
    sequence = list(sequence)
    # use the bits of seq_no to select items from sequence
    for seq_no in range(2**len(sequence)):
        yield tuple(value for (index, value) in enumerate(sequence) if 0x1 << index & seq_no)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
