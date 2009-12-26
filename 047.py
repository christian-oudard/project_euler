import itertools
from utility import prime_factorization, tuplewise

size = 4

def factor_counts():
    for n in itertools.count():
        yield len(set(prime_factorization(n)))

for n, counts in enumerate(tuplewise(size, factor_counts())):
    if all(c >= size for c in counts):
        print(n)
        break

# This can be done faster by going the other way, generating the number of
# prime factors for every number under a limit by enumerating primes and adding
# to a table of prime factor counts.
# Equivalently, a memoized prime_factorization function would run with the same
# complexity.
