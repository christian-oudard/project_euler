from utility import primes, up_to

def rot_left(s):
    """
    >>> rot_left('a')
    'a'
    >>> rot_left('abc')
    'bca'
    """
    return s[1:] + s[0]

def rotations(n):
    """
    >>> list(rotations(1))
    [1]
    >>> list(rotations(123))
    [123, 231, 312]
    """
    s = str(n)
    for _ in s:
        yield int(s)
        s = rot_left(s)

def circular_primes(limit):
    prime_set = set(up_to(limit, primes()))
    for p in prime_set:
        if all((r in prime_set) for r in rotations(p)):
            yield p

print(sum(1 for _ in circular_primes(1000000)))
