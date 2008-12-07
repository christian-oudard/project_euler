# this is horribly ineffecient
def primes_up_to(n):
	candidates = set(range(2, n+1))
	for i in up_to_sqrt_of(n):
		m = i
		while m <= n:
			m += i
			if m in candidates:
				candidates.remove(m)
	return sorted(list(candidates))

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

from math import sqrt
def up_to_sqrt_of(n):
	return range(2, int(sqrt(n)) + 1)
