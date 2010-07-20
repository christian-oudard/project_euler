# The minimum totient compared to the size of n will always be from the product
# of successive primes.

from utility import primes

limit = 1000000
last = None
result = 1
for p in primes():
    result *= p
    if result > limit:
        print(last)
        break
    last = result
