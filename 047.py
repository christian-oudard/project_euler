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
