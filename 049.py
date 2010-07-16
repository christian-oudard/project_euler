from collections import defaultdict
from utility import primes, digits_of, from_digits, all_pairs

def find_arithmetic_sequences(numbers, length):
    """
    Find arithmetic sequences in the given numbers of the specified length or longer.
    >>> list(find_arithmetic_sequences([1, 2, 3], 3))
    [(1, 2, 3)]
    >>> list(find_arithmetic_sequences([1, 3, 2], 3))
    [(1, 2, 3)]
    >>> list(find_arithmetic_sequences([1, 4, 5, 9, 10], 3))
    [(1, 5, 9)]
    """
    numbers = sorted(numbers)
    numbers_set = set(numbers)
    for a, b in all_pairs(numbers):
        assert a < b
        sequence = [a, b]
        diff = b - a
        c = b + diff
        while c in numbers_set:
            sequence.append(c)
            c = c + diff
            if len(sequence) >= length:
                yield tuple(sequence)
                break

if __name__ == '__main__':
    # Generate all four digit primes.
    four_digit_primes = []
    for p in primes():
        if p < 1000:
            continue
        four_digit_primes.append(p)
        if p >= 10000:
            break

    # Group primes by similar digits.
    primes_by_digits = defaultdict(list)
    for p in four_digit_primes:
        primes_by_digits[frozenset(digits_of(p))].append(p)

    # Strip out digit groups with less than three primes.
    for digits, primes in list(primes_by_digits.items()):
        if len(primes) < 3:
            del primes_by_digits[digits]

    # Look for arithmetic sequences of length 3.
    solutions = []
    for primes in primes_by_digits.values():
        for sequence in find_arithmetic_sequences(primes, 3):
            digits = []
            for n in sequence:
                digits.extend(digits_of(n))
            solutions.append(from_digits(digits))

    print(max(solutions))
