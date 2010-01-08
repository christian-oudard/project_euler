from utility import is_perfect_square, isqrt, up_to, figurate_numbers

def is_triangular_number(n):
    """
    >>> all(is_triangular_number(n) for n in up_to(1000000000, figurate_numbers(3)))
    True
    >>> any(is_triangular_number(n + 1) for n in up_to(1000000000, figurate_numbers(3)))
    False
    """
    #http://en.wikipedia.org/wiki/Triangular_number
    return is_perfect_square(8 * n + 1)

def is_pentagonal_number(n):
    """
    >>> all(is_pentagonal_number(n) for n in up_to(1000000000, figurate_numbers(5)))
    True
    >>> any(is_pentagonal_number(n + 1) for n in up_to(1000000000, figurate_numbers(5)))
    False
    """
    #http://en.wikipedia.org/wiki/Pentagonal_number
    h = 24 * n + 1
    r = isqrt(h)
    if r * r != h:
        return False
    return (r + 1) % 6 == 0


def is_hexagonal_number(n):
    """
    >>> all(is_hexagonal_number(n) for n in up_to(1000000000, figurate_numbers(6)))
    True
    >>> any(is_hexagonal_number(n + 1) for n in up_to(1000000000, figurate_numbers(6)))
    False
    """
    #http://en.wikipedia.org/wiki/Hexagonal_number
    h = 8 * n + 1
    r = isqrt(h)
    if r * r != h:
        return False
    return (r + 1) % 4 == 0

def tri_pent_hex_numbers():
    for n in figurate_numbers(6):
        if is_triangular_number(n) and is_pentagonal_number(n):
            yield n

gen = tri_pent_hex_numbers()
next(gen) # 1
next(gen) # 40755
print(next(gen))
