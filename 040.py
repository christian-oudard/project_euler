import itertools
from utility import digits_of, product

def iter_counting_digits():
    """
    >>> from utility import nth
    >>> nth(12 - 1, iter_counting_digits())
    1
    >>> ''.join(str(d) for d in itertools.islice(iter_counting_digits(), 33))
    '123456789101112131415161718192021'
    """
    for i in itertools.count(1):
        for d in digits_of(i):
            yield d

nums = {10**p - 1 for p in range(7)}
max_num = max(nums)
results = []
for i, d in enumerate(iter_counting_digits()):
    if i in nums:
        results.append(d)
        if len(results) >= len(nums):
            break
print(product(results))
