#! /usr/bin/python3

import sys

if __name__ == '__main__':
    try:
        limit = int(sys.argv[1])
    except (IndexError, ValueError):
        limit = 100
    print('generating the first %d primes' % limit)

    with open('primes_precalc.py', 'w') as f:
        import utility
        utility.prime_number(limit - 1)
        print('_primes =', utility._primes, file=f)
        print('_composites =', utility._composites, file=f)
