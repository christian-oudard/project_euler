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

def ilog(n, base):
    """
    Find the integer log of n with respect to the base.

    >>> import math
    >>> for base in range(2, 16 + 1):
    ...     for n in range(1, 1000):
    ...         assert ilog(n, base) == int(math.log(n, base) + 1e-10), '%s %s' % (n, base)
    """
    count = 0
    while n >= base:
        count += 1
        n //= base
    return count

def sci_notation(n, prec=3):
    """
    Represent n in scientific notation, with the specified precision.

    >>> sci_notation(1234 * 10**1000)
    '1.234e+1003'
    >>> sci_notation(10**1000 // 2, prec=1)
    '5.0e+999'
    """
    base = 10
    exponent = ilog(n, base)
    mantissa = n / base**exponent
    return '{0:.{1}f}e{2:+d}'.format(mantissa, prec, exponent)

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

def figurate_numbers(size):
    """
    >>> list(up_to(100, figurate_numbers(3))) # triangular numbers
    [1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 78, 91]
    >>> list(up_to(100, figurate_numbers(4))) # square numbers
    [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
    >>> list(up_to(100, figurate_numbers(5))) # pentagonal numbers
    [1, 5, 12, 22, 35, 51, 70, 92]
    >>> list(up_to(100, figurate_numbers(6))) # hexagonal numbers
    [1, 6, 15, 28, 45, 66, 91]
    """
    assert size >= 3
    step = size - 2
    n = 1
    d = n + step
    while True:
        yield n
        n += d
        d += step

def primes():
    """
    >>> list(up_to(100, primes()))
    [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    """
    for n in itertools.count():
        yield _prime_number(n)

def _prime_number(n):
    """
    Calculate the nth prime (0-based index).

    >>> _prime_number(1000 - 1)
    7919
    """
    while len(_primes) <= n:
        _gen_prime()
    return _primes[n]

_primes = [2] # Primes found so far.
_composites = {4: 2} # A mapping from composite numbers to the smallest prime
                     # that is a factor of it (its witness).
def _gen_prime():
    for n in itertools.count(_primes[-1] + 1):
        if n not in _composites:
            _primes.append(n) # Not a composite, therefore prime
            _composites[n**2] = n # The next unseen composite number is n squared.
            return
        else:
            # n is composite. Find the next unseen composite number with the
            # same witness as n.
            witness = _composites.pop(n)
            next = n + witness
            while next in _composites:
                next += witness
            _composites[next] = witness

def prime_factorization(n):
    """
    Return the prime factors of n, as a tuple, including repeats.

    >>> prime_factorization(12)
    (2, 2, 3)
    >>> prime_factorization(600851475143)
    (71, 839, 1471, 6857)

    >>> pf = prime_factorization(2**2000)
    >>> len(pf)
    2000
    >>> all(f == 2 for f in pf)
    True

    >>> all(n == product(prime_factorization(n)) for n in range(-100, 100))
    True
    """
    #TODO: improve algorithm so it can factor this number:
    # >>> prime_factorization(1543267864443420616877677640751301)
    # (27778299663977101, 55556599327954201)
    if n < 0:
        return (-1,) + prime_factorization(-n)
    if n == 0:
        return (0,)
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
    """
    Miller-Rabin primality test.

    A return value of False means n is certainly not prime. A return value of
    True means n is very likely a prime.

    >>> is_prime(1)
    False
    >>> is_prime(2)
    True
    >>> is_prime(3)
    True
    >>> is_prime(4)
    False
    >>> is_prime(5)
    True
    >>> is_prime(123456789)
    False

    >>> [i for i in range(10000) if is_prime(i)] == list(up_to(10000, primes()))
    True

    >>> pseudoprimes = [
    ...     75792980677,
    ...     21652684502221,
    ...     3825123056546413051,
    ...     318665857834031151167461,
    ...     3317044064679887385961981,
    ...     6003094289670105800312596501,
    ...     59276361075595573263446330101,
    ...     564132928021909221014087501701,
    ...     1543267864443420616877677640751301,
    ...     803837457453639491257079614341942108138837688287558145837488917\
522297427376533365218650233616396004545791504202360320876656996\
676098728404396540823292873879185086916685732826776177102938969\
773947016708230428687109997439976544144845341155872450633409279\
022275296229414984230688168540432645753401832978611129896064484\
5216191652872597534901,
    ... ]
    >>> any(is_prime(ps) for ps in pseudoprimes)
    False

    >>> is_prime(6438080068035544392301298549614926991513861075340134\
3291807343952413826484237063006136971539473913409092293733259038472039\
7133335969549256322620979036686633213903952966175107096769180017646161\
851573147596390153)
    True

    >>> is_prime(2**61 - 1)
    True
    >>> is_prime(2**89 - 1)
    True
    >>> is_prime(2**607 - 1)
    True
    >>> is_prime(2**601 - 1)
    False
    """
    # Test for n in small primes.
    small_primes = list(itertools.islice(primes(), 50))
    if n <= max(small_primes):
        return n in small_primes

    # Test for even numbers.
    if n & 1 == 0:
        return False

    # Use known pseudoprimes to prove primality within certain bounds.
    # References:
    # http://primes.utm.edu/prove/prove2_3.html
    # http://www.trnicely.net/misc/mpzspsp.html
    # http://mathworld.wolfram.com/StrongPseudoprime.html
    def test_all(*bases):
        return not any(test_composite(n, b) for b in bases)
    if n < 1373653:
        return test_all(2, 3)
    if n < 170584961:
        return test_all(350, 3958281543)
    if n < 75792980677:
        return test_all(2, 379215, 457083754)
    if n < 21652684502221:
        return test_all(2, 1215, 34862, 574237825)
    if n < 10**16:
        return test_all(2, 3, 7, 61, 24251)
    if n < 3317044064679887385961981:
        return test_all(*small_primes[:13])
    # Fallback, test first fifty primes.
    return test_all(*small_primes)

def test_composite(n, base):
    """
    Perform a Miller-Rabin strong pseudoprime test for the base a. Return
    True if n is definitely composite, or False if n is probably prime.
    """
    s, d = _factor_pow2(n - 1)
    b = pow(base, d, n)
    if b == 1:
        return False
    for _ in range(s):
        if b == n-1:
            return False
        b = b**2 % n
    return True # n is definitely composite

def _factor_pow2(n):
    """
    Factor powers of two from n. Return (s, d), with d odd, such that
    n = 2**s * d.
    """
    s = 0
    d = n
    while not d & 1:
        d >>= 1
        s += 1
    assert 2**s * d == n
    return s, d

def totient(n):
    """
    Euler's totient function.
    Find the number of positive integers less than or equal to n that are coprime to n.

    >>> [totient(n) for n in range(1, 70)]
    [1, 1, 2, 2, 4, 2, 6, 4, 6, 4, 10, 4, 12, 6, 8, 8, 16, 6, 18, 8, 12, 10, 22, 8, 20, 12, 18, 12, 28, 8, 30, 16, 20, 16, 24, 12, 36, 18, 24, 16, 40, 12, 42, 20, 24, 22, 46, 16, 42, 20, 32, 24, 52, 18, 40, 24, 36, 28, 58, 16, 60, 30, 36, 32, 48, 20, 66, 32, 44]
    >>> totient(0)
    0
    """
    if n == 0:
        return 0
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

def divide_ceil(a, b):
    """
    Integer division, rounding up instead of down.
    >>> divide_ceil(5, 2)
    3
    """
    q, r = divmod(a, b)
    if r > 0:
        q += 1
    return q

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

def nth(n, iterable):
    """
    Get the Nth item in the iterable, 0-based.

    >>> s = 'abcd'
    >>> nth(0, s)
    'a'
    >>> nth(3, s)
    'd'
    >>> nth(4, s)
    Traceback (most recent call last):
        ...
    IndexError: list index out of range
    """
    return list(itertools.islice(iterable, n, n+1))[0]

def max_key(pair_sequence, key_func=None):
    """
    Return the key in the sequence that corresponds to the maximum value.

    >>> max_key([('apples', 3), ('bananas', 7)])
    'bananas'
    >>> max_key([('apples', [1, 2, 3]), ('bananas', [3, 2])], key_func=len)
    'apples'
    """
    if not key_func:
        key_func = lambda x: x
    pair_sequence = iter(pair_sequence)
    max_key, max_value = next(pair_sequence)
    max_value = key_func(max_value)
    for key, value in pair_sequence:
        value = key_func(value)
        if value > max_value:
            max_key, max_value = key, value
    return max_key

def frequency_count(l):
    """
    >>> fc = frequency_count('aaabbc')
    >>> sorted(fc.items())
    [('a', 3), ('b', 2), ('c', 1)]
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

def all_pairs(iterable):
    """
    Iterate over all possible pairs in the iterable, in lexicographic order.

    >>> list(''.join(pair) for pair in all_pairs('abcd'))
    ['ab', 'ac', 'ad', 'bc', 'bd', 'cd']
    """
    iterable = list(iterable)
    for i, a in enumerate(iterable):
        for b in iterable[i+1:]:
            yield (a, b)

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
    >>> ncr(10000, 1000) == ncr(10000, 9000)
    True
    """
    assert 0 <= r <= n
    if r > n // 2:
        r = n - r
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

def from_digits(digits, base=10):
    """
    Reconstruct an integer from its digits.

    >>> from_digits([1, 2, 3])
    123
    >>> from_digits([10, 11, 12], base=16) == 0xabc
    True
    >>> all(n == from_digits(digits_of(n)) for n in range(10000))
    True
    """
    result = 0
    power = 1
    for digit in reversed(digits):
        result += power * digit
        power *= base
    return result

def digital_root(n, base=10):
    """
    Repeatedly sum the digits of N until there is a single digit left.
    """
    # Using the congruence method, see:
    # http://en.wikipedia.org/wiki/Digital_root
    result = n % (base - 1)
    if result == 0:
        return base - 1
    return result

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

