import math
from itertools import islice
from utility import is_probable_prime, primes, up_to

def prime_sqrt(n):
    """
    >>> prime_sqrt(4)
    (2, 2)
    >>> prime_sqrt(1000)
    (31, 37)
    """
    if n < 4:
        raise ValueError(n)
    s = math.sqrt(n)
    lps = math.floor(s)
    while not is_probable_prime(lps):
        lps -= 1
    ups = math.ceil(s)
    while not is_probable_prime(ups):
        ups += 1
    return (lps, ups)

def is_semidivisible(n):
    """
    >>> is_semidivisible(8)
    True
    >>> is_semidivisible(10)
    True
    >>> is_semidivisible(12)
    True
    >>> is_semidivisible(9)
    False
    """
    lps, ups = prime_sqrt(n)
    return (n % lps == 0) + (n % ups == 0) == 1

def semidivisible_numbers(limit):
    """
    >>> list(semidivisible_numbers(1000))
    [8, 10, 12, 18, 20, 21, 24, 28, 30, 40, 42, 45, 55, 56, 63, 66, 70, 84, 88, 91, 98, 99, 105, 110, 112, 119, 130, 132, 154, 156, 165, 170, 182, 187, 195, 204, 208, 234, 238, 247, 255, 260, 272, 273, 286, 304, 306, 340, 342, 357, 368, 380, 391, 399, 414, 418, 456, 460, 475, 483, 494, 506, 513, 551, 552, 575, 580, 598, 609, 621, 638, 644, 690, 696, 713, 725, 736, 754, 759, 782, 783, 805, 812, 828, 868, 870, 928, 930, 957, 962, 992, 999]
    >>> len(_)
    92
    """
    for lps, ups in zip(primes(), islice(primes(), 1, None)): 
        lo = lps**2
        hi = ups**2 

        hi_candidates = set()
        lo_candidates = set()

        c = hi - ups
        while c > lo:
            hi_candidates.add(c)
            c -= ups

        c = lo + lps
        while c < hi:
            lo_candidates.add(c)
            c += lps

        candidates = lo_candidates.symmetric_difference(hi_candidates)
        for c in sorted(list(candidates)):
            if c > limit:
                return
            yield c

print(sum(semidivisible_numbers(999966663333)))
