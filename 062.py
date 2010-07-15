from utility import digits_of, all_equal

def cube_permutations(size):
    """
    >>> cube_permutations(3)
    {345, 384, 405}
    """
    pass

if __name__ == '__main__':
    # Verify given solution.
    digits = [sorted(digits_of(n**3)) for n in {345, 384, 405}]
    assert all_equal(digits)
