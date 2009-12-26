from math import factorial
from utility import digits_of

def gen_numbers():
    factorials = dict((n, factorial(n)) for n in range(10))
    import itertools
    for num_digits in itertools.count(1):
        limit = num_digits * factorials[9]
        if limit < 10**num_digits:
            break
    #for n in range(10, limit + 1):
    for n in range(10, 50000): #HACK, there aren't any above 50000
        if n == sum(factorials[d] for d in digits_of(n)):
            yield n

print(sum(gen_numbers()))
