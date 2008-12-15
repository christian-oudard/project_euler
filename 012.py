import itertools
from utility import up_to, prime_factorization, frequency_count, product

def main():
    target = 500
    for t in up_to(100000000, triangle_numbers()):
        num = num_divisors(t) 
        if num > target:
            print(t)
            break

def triangle_numbers():
    t = 1
    n = 1
    while True:
        yield t
        n += 1
        t += n

def divisors_naive(n):
    for d in range(1, n+1):
        if n % d == 0:
            yield d

def num_divisors(n):
    """
    >>> num_divisors(12)
    6
    >>> num_divisors(28)
    6
    """
    pf = prime_factorization(n)
    # build up all combinations of prime factors
    # turn each repeated factor into a stack of powers,
    # e.g. [2, 2, 2] -> 2, 4, 8
    # for each combination of n stacks,
    # add every possible
    fc = frequency_count(pf)
    num_divisors = 0
    for r in range(len(fc) + 1):
        for combo in itertools.combinations(fc.values(), r):
            num_divisors += product(combo)
    return num_divisors

if __name__ == '__main__':
    main()
    #import doctest
    #doctest.testmod()

    
