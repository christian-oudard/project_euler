import itertools
from utility import totient, up_to, primes, isqrt, memoize

#limit = 10**6
limit = 6

#totients_naive = [totient(n) for n in range(limit)]

@memoize
def totient_recursive(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    for prime in up_to(isqrt(n), primes()):
        quotient, remainder = divmod(n, prime)
        if remainder == 0:
            t = totient_recursive(quotient)
            if quotient % prime == 0:
                return t * prime
            else:
                return t * (prime - 1)
    else:
        return n - 1

for n in range(limit):
    t = totient_recursive(n)

#for n in range(1, 50):
#    tn = totient(n)
#    t2n = totient(2*n)
#    t3n = totient(3*n)
#    t5n = totient(5*n)
#    ratio = t5n / tn
#    #print(' '.join('%s' % i for i in [n, ratio, tn, t5n]))
#
#    # double rule
#    if n % 2 == 0:
#        assert tn * 2 == t2n
#    else:
#        assert tn == t2n
#
#    # triple rule
#    if n % 3 == 0:
#        assert tn * 3 == t3n
#    else:
#        assert tn * 2 == t3n
#
#    # X5 rule
#    if n % 5 == 0:
#        assert tn * 5 == t5n
#    else:
#        assert tn * 4 == t5n
#
#    # etc.
