#! /usr/bin/python3

import math
import itertools
import random
import functools
from copy import copy
from collections import defaultdict

def memoize(func):
    func._cache = {}
    def memoize(*args, **kwargs):
        if kwargs: # frozenset is used to ensure hashability
            key = args, frozenset(kwargs.items())
        else:
            key = args
        cache = func._cache
        if key in cache:
            return cache[key]
        else:
            cache[key] = result = func(*args, **kwargs)
            return result
    return functools.update_wrapper(memoize, func)

def primes():
    """
    >>> list(up_to(100, primes()))
    [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    """
    for n in itertools.count():
        yield prime_number(n)

def prime_number(n):
    """
    Calculate the nth prime (0-based index).

    >>> prime_number(1000 - 1)
    7919
    """
    for i in range(n - len(_primes) + 1):
        _gen_prime()
    return _primes[n]

_p_calcs = 0
_primes = [2]
_composites = {4: 2}
try:
    from primes_precalc import _primes, _composites
except ImportError:
    pass
def _gen_prime():
    global _p_calcs
    for n in itertools.count(_primes[-1] + 1):
        if n not in _composites:
            # not a composite, therefore prime
            _primes.append(n)
            _composites[n**2] = n # the next unseen composite number here will be n squared
            _p_calcs += 1
            return
        else: # n is a composite number
            # find the next unseen composite number with the same witness as n
            witness = _composites.pop(n)
            next = n + witness
            while next in _composites:
                next += witness
            _composites[next] = witness

@memoize
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
    assert n > 0
    if n == 1:
        return []
    for p in up_to(math.ceil(math.sqrt(n)), primes()):
        quotient, remainder = divmod(n, p)
        if remainder == 0:
            return [p] + prime_factorization(quotient)
    return [n]

def is_prime(n):
    # Check prime cache.
    if n <= _primes[-1]:
        return n in _primes
    return _is_prime(n)

def _is_prime(n):
    if n < 2:
        return False
    for i in up_to_sqrt_of(n):
        if n % i == 0:
            return False
    return True

_mrpt_num_trials = 5 # number of bases to test
def is_probable_prime(n):
    """
    Miller-Rabin primality test.

    A return value of False means n is certainly not prime. A return value of
    True means n is very likely a prime.

    >>> is_probable_prime(1)
    Traceback (most recent call last):
        ...
    AssertionError
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

    >>> primes_under_1000 = [i for i in range(2, 1000) if is_probable_prime(i)]
    >>> len(primes_under_1000)
    168
    >>> primes_under_1000[-10:]
    [937, 941, 947, 953, 967, 971, 977, 983, 991, 997]

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
    assert n >= 2
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

    # test the base a to see whether it is a witness for the compositeness of n
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
    return True # no base tested showed n as composite

def totient(n):
    """
    Euler's totient function.
    Find the number of positive integers less than or equal to n that are coprime to n.

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

def coprime(a, b):
    """
    >>> coprime(6, 35)
    True
    >>> coprime(6, 27)
    False
    """
    return gcd(a, b) == 1

def up_to(n, iterable):
    """Yield values from the iterable up to and including n."""
    return itertools.takewhile(lambda i: i <= n, iterable)

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

def pairwise(iterable):
    """s -> (s0,s1), (s1,s2), (s2, s3), ...

    >>> list(pairwise([1, 2, 3, 4]))
    [(1, 2), (2, 3), (3, 4)]
    """
    a, b = itertools.tee(iterable)
    next(b, None)
    return zip(a, b)

def tuplewise(n, iterable):
    """
    >>> list(tuplewise(2, [1, 2, 3, 4]))
    [(1, 2), (2, 3), (3, 4)]
    >>> list(tuplewise(3, [1, 2, 3, 4]))
    [(1, 2, 3), (2, 3, 4)]
    """
    iters = itertools.tee(iterable, n)
    for repeat, iter in enumerate(iters):
        for i in range(repeat):
            next(iter)
    return zip(*iters)

def npr(n, r):
    """
    Calculate the number of ordered permutations of r items taken from a
    population of size n.

    >>> npr(3, 2)
    6
    >>> npr(100, 20)
    1303995018204712451095685346159820800000
    >>> npr(50000, 5000) % 123456789123456789
    95689049376143223
    """
    assert 0 <= r <= n
    return product(range(n - r + 1, n + 1))

def ncr(n, r):
    """
    Calculate the number of unordered combinations of r items taken from a
    population of size n.

    >>> ncr(3, 2)
    3
    >>> ncr(100, 20)
    535983370403809682970
    >>> ncr(50000, 5000) % 123456789123456789
    8758576905993486
    """
    assert 0 <= r <= n
    return npr(n, r) // math.factorial(r)

def digits_of(n):
    """
    Split the number into its digits.

    >>> digits_of(123)
    [1, 2, 3]
    """
    digits = []
    while n > 0:
        n, d = divmod(n, 10)
        digits.insert(0, d)
    return digits

if __name__ == '__main__':
    import doctest
    import time
    start = time.time()
    doctest.testmod()
    end = time.time()
    print('%.3fs' % (end - start))

