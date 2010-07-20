from utility import up_to, is_prime

def spiral_corners():
    """
    37 36 35 34 33 32 31
    38 17 16 15 14 13 30
    39 18  5  4  3 12 29
    40 19  6  1  2 11 28
    41 20  7  8  9 10 27
    42 21 22 23 24 25 26
    43 44 45 46 47 48 49

    >>> import itertools
    >>> list(itertools.islice(spiral_corners(), 4))
    [(1,), (3, 5, 7, 9), (13, 17, 21, 25), (31, 37, 43, 49)]
    """
    size = 0
    n = 1
    yield (n,)
    while True:
        size += 2
        nums = []
        for _ in range(4):
            n += size
            nums.append(n)
        yield tuple(nums)

if __name__ == '__main__':
    total = 0
    prime_count = 0
    for i, nums in enumerate(spiral_corners()):
        for n in nums:
            total += 1
            if is_prime(n):
                prime_count += 1
        if i > 0 and prime_count * 10 < total:
            print(2 * i + 1)
            break
