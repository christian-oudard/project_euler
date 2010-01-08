#! /usr/bin/python3

import itertools
import random
import functools
from math import factorial
from collections import defaultdict

import vec

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

# adapted from http://www.codecodex.com/wiki/Calculate_an_integer_square_root
def isqrt(n):
    """
    Integer floor square root. Handles large numbers.

    >>> import math
    >>> [isqrt(n) for n in range(1000)] == [math.floor(math.sqrt(n)) for n in range(1000)]
    True
    >>> isqrt(2**2000) == 2**1000
    True

    >>> n = 188198812920607963838697239461650439807163563379417382700763356422988859715234665485319060606504743045317388011303396716199692321205734031879550656996221305168759307650257059
    >>> r = isqrt(n)
    >>> r
    433818871097844202389623285336968290605469456301558930293445695571862781832679867424802
    >>> r**2 <= n
    True
    >>> (r + 1)**2 > n
    True
    """
    guess = (n >> n.bit_length() // 2) + 1
    result = (guess + n // guess) // 2
    while abs(result - guess) > 1:
        guess = result
        result = (guess + n // guess) // 2
    while result * result > n:
        result -= 1
    return result

def is_perfect_square(n):
    """
    Test to see if n is a perfect square.

    >>> is_perfect_square(-1)
    False
    >>> is_perfect_square(0)
    True
    >>> is_perfect_square(3)
    False
    >>> is_perfect_square(4)
    True

    >>> limit = 10000
    >>> squares = set(n**2 for n in range(isqrt(limit) + 1))
    >>> all(is_perfect_square(n) for n in squares)
    True
    >>> non_squares = set(range(limit)) - squares
    >>> any(is_perfect_square(n) for n in non_squares)
    False
    """
    if n < 0:
        return False
    if n == 0:
        return True
    # Perfect squares in hexadecimal can only end in 0, 1, 4, or 9.
    if (n & 0xf) not in (0, 1, 4, 9):
        return False
    # No quick tests showed n as non-square, just check the square root.
    return isqrt(n) ** 2 == n

def primes():
    """
    >>> list(up_to(100, primes()))
    [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    """
    composites = {} # A mapping from composite numbers to the smallest prime
                    # that is a factor of it (its witness).
    n = 2 # The current number being considered as a prime.
    while True:
        if n not in composites:
            yield n # Not a composite, therefore prime.
            composites[n**2] = n # The next unseen composite number is n squared.
        else:
            # n is composite. Find the next unseen composite number with the
            # same witness as n.
            witness = composites.pop(n)
            next = n + witness
            while next in composites:
                next += witness
            composites[next] = witness
        n += 1
    for n in itertools.count():
        yield prime_number(n)

def primes_up_to(limit):
    """
    >>> primes_up_to(100)
    [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    >>> len(primes_up_to(1000000))
    78498
    """
    return list(up_to(limit, primes()))

@memoize
def prime_factorization(n):
    """
    Return the prime factors of n, as a tuple, including repeats.

    >>> prime_factorization(1)
    ()
    >>> prime_factorization(2)
    (2,)
    >>> prime_factorization(4)
    (2, 2)
    >>> prime_factorization(8)
    (2, 2, 2)
    >>> prime_factorization(12)
    (2, 2, 3)
    >>> prime_factorization(600851475143)
    (71, 839, 1471, 6857)

    >>> pf = prime_factorization(2**2000)
    >>> len(pf)
    2000
    >>> all(f == 2 for f in pf)
    True
    """
    assert n > 0

    if n == 1:
        return ()

    factors = []
    while True:
        for p in up_to(isqrt(n), primes()):
            quotient, remainder = divmod(n, p)
            if remainder == 0:
                factors.append(p)
                n = quotient
                break # Continue while loop.
        else:
            factors.append(n)
            factors = tuple(factors)
            return factors

def is_prime(n):
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
    False
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
    if n < 2:
        return False
    if n == 2:
        return True
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
    return range(2, isqrt(n) + 1)

def product(iterable):
    prod = 1
    for n in iterable:
        prod *= n
    return prod

def nth(iterable, n):
    """
    Get the Nth item in the iterable, 0-based.

    >>> s = 'abcd'
    >>> nth(s, 0)
    'a'
    >>> nth(s, 3)
    'd'
    >>> nth(s, 4)
    Traceback (most recent call last):
        ...
    IndexError: list index out of range
    """
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
    return npr(n, r) // factorial(r)

def digits_of(n, base=10):
    """
    Split the number into its digits.

    >>> digits_of(0)
    [0]
    >>> digits_of(123)
    [1, 2, 3]
    >>> digits_of(0xabc, base=16)
    [10, 11, 12]
    """
    if n == 0:
        return [0]
    digits = []
    while n > 0:
        n, d = divmod(n, base)
        digits.append(d)
    digits.reverse()
    return digits

def cmp(a, b):
    if a == b:
        return 0
    if a < b:
        return -1
    if a > b:
        return 1

def cmp_line(l1, l2, p):
    """
    Determine where the point p lies with relation to the line l1-l2.
    Return -1 if s is below, +1 if it is above, and 0 if it is on the line.

    >>> cmp_line((-1,-1), (1,1), (1,0))
    -1
    >>> cmp_line((-1,-1), (1,1), (0,1))
    1
    >>> cmp_line((-1,-1), (1,1), (0,0))
    0

    It also works with vertical lines.
    >>> cmp_line((0,-1), (0,1), (1, 0))
    -1
    >>> cmp_line((0,-1), (0,1), (-1, 0))
    1
    >>> cmp_line((0,-1), (0,1), (0, 0))
    0
    """
    x1, y1 = l1
    x2, y2 = l2
    x, y = p
    dy = y2 - y1
    dx = x2 - x1
    return cmp(y * dx, dy * (x - x1) + y1 * dx)

def partition(points, l1, l2, s=None):
    """
    Partition a set of points by a line.

    The line is defined by l1, l2. The desired side of the line is given by the point s.

    >>> partition([(-1,0), (0,0), (1,0)], (0,1), (0,-1), (2,0))[0]
    {(1, 0)}
    >>> partition([(-1,0), (0,0), (1,0)], (0,1), (0,-1), (-2,0))[0]
    {(-1, 0)}
    >>> partition([(-2,2), (-1,0), (0,0), (1,0)], (-1,0), (0,1), (3,0))[0] == {(0, 0), (1, 0)}
    True
    >>> partition([(-2,2), (-1,0), (0,0), (1,0)], (-1,0), (0,1), (-3,0))[0] == {(-2, 2)}
    True

    You can omit the argument "s" if you don't care.
    >>> partition([(-1,0), (0,0), (1,0)], (0,1), (0,-1))
    ({(-1, 0)}, {(1, 0)})
    """
    if s is None:
        s = vec.add(l1, vec.perp(vec.vfrom(l1, l2)))

    if l1 == l2:
        raise ValueError('l1 equals l2')
    sign = cmp_line(l1, l2, s)
    if sign == 0:
        raise ValueError('s is on the line l1 l2')

    forward = set()
    reverse = set()
    for p in points:
        c = cmp_line(l1, l2, p)
        if c == sign:
            forward.add(p)
        elif c == -sign:
            reverse.add(p)
    return forward, reverse


if __name__ == '__main__':
    import doctest
    import time
    start = time.time()
    doctest.testmod()
    end = time.time()
    print('%.3fs' % (end - start))

