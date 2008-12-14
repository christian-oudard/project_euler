import math
import time
import itertools

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

def up_to(n, iterable):
    return list(itertools.takewhile(lambda i: i <= n, iterable))

def prime_factorization(n):
    """
    Return the prime factors of n, as a list, including repeats.
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
            factors.append(n)
            return factors

def test_prime_factorization(limit=1000):
	for i in range(2, limit):
		pf = prime_factorization(i)
		#print pf
		for p in pf:
			assert(is_prime(p))
		assert(product(pf) == i)
		
def is_prime(n):
	if n < 2:
		return False
	for i in up_to_sqrt_of(n):
		if n % i == 0:
			return False
	return True

def up_to_sqrt_of(n):
	return range(2, math.ceil(math.sqrt(n)))

def product(iterable):
    prod = 1
    for n in iterable:
        prod *= n
    return prod

# not yet used
#def perfect_squares_up_to(n):
#    perfect_squares = set()
#    i = s = 1
#    while s <= n:
#        perfect_squares.add(s)
#        i += 1
#        s = i**2
#    return perfect_squares

def nth(iterable, n):
    """Get the Nth item in the iterable."""
    return list(itertools.islice(iterable, n, n+1))[0]

def all_pairs(iterable):
    enumerated_values = list(enumerate(iterable))
    for low_index, first_item in enumerated_values:
        for high_index, second_item in enumerated_values[low_index + 1:]:
            yield (first_item, second_item)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
