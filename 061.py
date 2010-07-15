from utility import figurate_numbers, product, ncr, digits_of, pairwise
from math import factorial
import itertools

def four_digit_figurate(size):
    for n in figurate_numbers(size):
        if n < 1000:
            continue
        if n >= 10000:
            break
        yield n

#print('number of 4 digit figurate numbers from 3 to 8')
#print(len(list(four_digit_figurate(3))))
#print(len(list(four_digit_figurate(4))))
#print(len(list(four_digit_figurate(5))))
#print(len(list(four_digit_figurate(6))))
#print(len(list(four_digit_figurate(7))))
#print(len(list(four_digit_figurate(8))))
#print('total')
#print(sum(len(list(four_digit_figurate(size))) for size in range(3, 8+1)))
#
#print('number of possible non-cyclic sets of size 6')
#print(product(len(list(four_digit_figurate(size))) for size in range(3, 8+1)))
#
#print('number of unique four digit figurate numbers from 3 to 8')
#n = len(set(itertools.chain(*[four_digit_figurate(size) for size in range(3, 8+1)])))
#print(n)
#
#print('{} choose {}'.format(n, 6), ncr(n, 6))

def is_connection(a, b):
    """
    >>> is_connection(1234, 3456)
    True
    """
    return (digits_of(a)[-2:] == digits_of(b)[:2])

def is_cyclic(nums):
    """
    >>> is_cyclic([8128, 2882, 8281])
    True
    >>> is_cyclic([8228, 2882, 8281])
    False
    """
    for a, b in pairwise(nums):
        if not is_connection(a, b):
            return False
    if not is_connection(nums[-1], nums[0]):
        return False
    return True

def search():
    # Naive method

    for iterables in itertools.permutations([
        list(four_digit_figurate(3)),
        list(four_digit_figurate(4)),
        list(four_digit_figurate(5)),
    ], 3):
        for a, b, c in itertools.product(*iterables):
            if is_cyclic([a, b, c]):
                return [a, b, c]
print(search())
