import itertools
from utility import digits_of, from_digits, primes

def truncations(digits):
    """
    Remove digits from the left and from the right, giving new numbers.

    >>> list(truncations([1, 2, 3, 4]))
    [(2, 3, 4), (1, 2, 3), (3, 4), (1, 2), (4,), (1,)]
    """
    num_digits = len(digits)
    for i in range(1, num_digits):
        yield tuple(digits[i:])
        yield tuple(digits[:-i])

def truncatable_primes():
    seen_primes = set()
    one_digit_primes = (2, 3, 5, 7)
    for p in primes():
        seen_primes.add(p)
        digits = digits_of(p)
        # One-digit primes are not considered truncatable.
        if len(digits) == 1:
            continue
        # All digits besides the first must be odd.
        if not all(d % 2 == 1 for d in digits[1:]):
            continue
        # First and last digit must be prime.
        if digits[0] not in one_digit_primes or \
           digits[-1] not in one_digit_primes:
            continue
        # Test whether each truncation is a prime.
        truncs = sorted(list(from_digits(d) for d in truncations(digits)))
        if all(t in seen_primes for t in truncs):
            yield p

print(sum(itertools.islice(truncatable_primes(), 11)))
