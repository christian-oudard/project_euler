from utility import figurate_numbers, up_to, isqrt

def is_pentagonal(n):
    """
    >>> limit = 1000
    >>> pentagonal_numbers = set(up_to(limit, figurate_numbers(5)))
    >>> for n in range(limit + 1):
    ...     assert is_pentagonal(n) == (n in pentagonal_numbers)
    """
    # Test condition adapted from http://en.wikipedia.org/wiki/Pentagonal_number
    a = 24 * n + 1
    sqrt_a = isqrt(a)
    if sqrt_a ** 2 != a:
        return False
    return (sqrt_a + 1) % 6 == 0

def all_pairs_infinite(iterable):
    """
    Iterate over all possible pairs in the iterable, allowing for infinite
    iterables.

    >>> list(itertools.islice(all_pairs_infinite(itertools.count()), 7))
    [(1, 0), (2, 0), (2, 1), (3, 0), (3, 1), (3, 2), (4, 0)]
    """
    iterable = iter(iterable)
    seen = [next(iterable)]
    for a in iterable:
        for b in seen:
            yield a, b
        seen.append(a)

for a, b in all_pairs_infinite(figurate_numbers(5)):
    if is_pentagonal(a + b) and is_pentagonal(a - b):
        print(a - b)
        break
