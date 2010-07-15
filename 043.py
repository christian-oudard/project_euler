import itertools
from utility import from_digits, tuplewise

primes = [2, 3, 5, 7, 11, 13, 17]
def check(digits):
    """
    >>> from utility import digits_of
    >>> check(digits_of(1406357289))
    True
    >>> check(digits_of(1406357298))
    False
    """
    digits = digits[1:] # ignore the first number
    for prime, number in zip(primes, tuplewise(3, digits)):
        number = from_digits(number)
        if not number % prime == 0:
            return False
    return True

solutions = []
for digits in itertools.permutations(range(10)):
    if check(digits):
        solutions.append(from_digits(digits))

print(sum(solutions))
