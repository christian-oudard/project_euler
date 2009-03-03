from copy import copy
from math import factorial
from utility import nth

def permutation_ids(length):
    """
    >>> list(permutation_ids(4))
    [(0, 0, 0), (0, 0, 1), (0, 1, 0), (0, 1, 1), (0, 2, 0), (0, 2, 1), (1, 0, 0), (1, 0, 1), (1, 1, 0), (1, 1, 1), (1, 2, 0), (1, 2, 1), (2, 0, 0), (2, 0, 1), (2, 1, 0), (2, 1, 1), (2, 2, 0), (2, 2, 1), (3, 0, 0), (3, 0, 1), (3, 1, 0), (3, 1, 1), (3, 2, 0), (3, 2, 1)]
    """
    perm_id = [0] * (length - 1)
    while perm_id[0] < length:
        yield tuple(perm_id)
        perm_id[-1] += 1 # increment the last item
        # carry overflow, and cascade
        for rindex in range(1, length - 1):
            if perm_id[-rindex] > rindex:
                perm_id[-rindex] = 0
                perm_id[-rindex - 1] += 1

def perm_from_id(sequence, id):
    """
    >>> perm_from_id('abc', (0, 0))
    ('a', 'b', 'c')
    >>> perm_from_id('abc', (2, 1))
    ('c', 'b', 'a')
    """
    sequence = copy(list(sequence))
    perm = []
    for index in id:
        perm.append(sequence.pop(index))
    perm.append(sequence.pop())
    return tuple(perm)

def permutations(sequence):
    """
    >>> [''.join(p) for p in permutations('abc')]
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']
    >>> s = 'abcdefg'
    >>> perms = [''.join(p) for p in permutations(s)]
    >>> perms == sorted(perms)
    True
    >>> len(perms) == factorial(len(s))
    True
    """
    for id in permutation_ids(len(sequence)):
        yield perm_from_id(sequence, id)

def nth_perm_id(length, n):
    """
    >>> list(permutation_ids(4))[10]
    (1, 2, 0)
    >>> nth_perm_id(4, 10)
    (1, 2, 0)
    >>> list(permutation_ids(6)) == [nth_perm_id(6, i) for i in range(factorial(6))]
    True
    """
    perm_id = [0] * (length - 1)
    for rindex in range(1, length):
        perm_id[-rindex] = n // factorial(rindex) % (rindex + 1)
    return tuple(perm_id)

if __name__ == '__main__':
    id = nth_perm_id(10, 1000000 - 1)
    perm = perm_from_id(range(10), id)
    number = ''.join(str(d) for d in perm)
    print(number)
