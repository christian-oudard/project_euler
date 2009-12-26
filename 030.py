from utility import digits_of

def sum_of_powers(n, p):
    """
    >>> sum_of_powers(34, 2)
    25
    >>> sum_of_powers(1634, 4)
    1634
    >>> sum_of_powers(8208, 4)
    8208
    >>> sum_of_powers(9474, 4)
    9474
    """
    return sum(d**p for d in digits_of(n))


def find_numbers(power):
    import itertools
    for num_digits in itertools.count(1):
        limit = num_digits * 9**power
        if limit < 10**num_digits:
            break
    for n in range(2, limit):
        if n == sum_of_powers(n, 5):
            yield n

print(sum(find_numbers(5)))
