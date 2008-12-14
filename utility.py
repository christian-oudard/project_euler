from math import sqrt
import time
import itertools

def primes():
    composites = {} # a mapping from composite numbers to the smallest prime that is a factor of it (its witness)
    n = 2 # the current number being considered as a prime
    while True:
        if n not in composites:
            # not a composite, therefore prime
            yield n
            composites[n**2] = n # the next unseen composite number here will be n squared
        else: # n is a composite number
            # find the next unseen composite number with the same witness as n
            witness = composites.pop(n)
            next = n + witness
            while next in composites:
                next += witness
            composites[next] = witness
        n += 1

def up_to(n, iterable):
    return list(itertools.takewhile(lambda i: i <= n, iterable))

def prime_factorization(n):
	""" Return the prime factors of n, as a list, including repeats. """
	factors = [n]

	def next_split():
		for f in factors:
			for i in up_to_sqrt_of(f):
				if f % i == 0:
					return f, (i, f//i)

	while True:
		s = next_split()
		if not s: 
			break
		f, (a, b) = s
		factors.remove(f)
		factors.extend((a, b))

	return sorted(factors)
			
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
	return range(2, int(sqrt(n)) + 1)

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

