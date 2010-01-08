import itertools
from utility import digits_of

limit = 6
for n in itertools.count(1):
    digits_n = sorted(digits_of(n))
    if all(sorted(digits_of(n * m)) == digits_n for m in range(2, limit + 1)):
        break
print(n)
