from utility import digits_of, from_digits

def reverse_and_add(n):
    """
    >>> reverse_and_add(47)
    121
    >>> reverse_and_add(349)
    1292
    >>> reverse_and_add(1292)
    4213
    >>> reverse_and_add(4213)
    7337
    """
    rev_n = from_digits(list(reversed(digits_of(n))))
    return n + rev_n

def is_palindromic(n):
    """
    >>> is_palindromic(121)
    True
    >>> is_palindromic(7337)
    True
    >>> any(is_palindromic(n) for n in [47, 349, 1292, 4213])
    False
    """
    digits = digits_of(n)
    return digits == list(reversed(digits))

def is_lychrel(n):
    """
    >>> is_lychrel(47)
    False
    >>> is_lychrel(349)
    False
    >>> is_lychrel(196)
    True
    >>> is_lychrel(4994)
    True
    """
    for _ in range(50):
        n = reverse_and_add(n)
        if is_palindromic(n):
            return False
    return True

count = 0
for n in range(10000):
    if is_lychrel(n):
        count += 1
print(count)
