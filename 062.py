import itertools
from collections import defaultdict
from utility import digits_of, all_equal

#The cube, 41063625 (3453), can be permuted to produce two other cubes: 56623104 (3843) and 66430125 (4053). In fact, 41063625 is the smallest cube which has exactly three permutations of its digits which are also cube.
#
#Find the smallest cube for which exactly five permutations of its digits are cube.
def cube_permutations(size):
    """
    >>> sorted(cube_permutations(3))
    [345, 384, 405]
    """
    cubes_by_digits = defaultdict(list)
    for i in itertools.count(1):
        cube = i**3
        digits = tuple(sorted(digits_of(cube)))
        cubes = cubes_by_digits[digits]
        cubes.append(i)
        if len(cubes) >= size:
            return set(cubes)

if __name__ == '__main__':
    print(min(cube_permutations(5)) ** 3)
