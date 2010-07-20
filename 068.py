import itertools

def is_magic(nums):
    """
    >>> is_magic([4, 5, 6, 2, 3, 1])
    [4, 2, 3, 5, 3, 1, 6, 1, 2]
    >>> is_magic([1, 3, 2, 6, 5, 4])
    [1, 6, 5, 3, 5, 4, 2, 4, 6]
    >>> is_magic([6, 4, 5, 1, 2, 3])
    False
    """
    size = len(nums) // 2
    outer = nums[:size]
    inner = nums[size:]

    if min(outer) != outer[0]:
        return False # Not in canonical form

    canonical = []
    sums = None
    for i in range(size):
        a = outer[i]
        b = inner[i]
        c = inner[(i + 1) % size]
        canonical.extend((a, b, c))
        total = sum((a, b, c))
        if not sums:
            sums = [total]
        else:
            if total != sums[-1]:
                return False
    return canonical


if __name__ == '__main__':
    numbers = list(range(1, 10 + 1))

    solutions = []
    for nums in itertools.permutations(numbers):
        result = is_magic(nums)
        if result:
            solutions.append(result)

    strings = [''.join(str(n) for n in sol) for sol in solutions]
    strings = [s for s in strings if len(s) == 16]
    print(max(strings))

