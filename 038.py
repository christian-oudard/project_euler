import itertools
from utility import digits_of, from_digits

target_digits = set(range(1, 10))
solutions = []
for limit in [2, 3, 4, 5]:
    for i in itertools.count(1):
        digits = []
        for m in range(1, limit + 1):
            digits.extend(digits_of(m * i))
        if 0 in digits:
            continue
        if len(digits) < 9:
            continue
        if len(digits) > 9:
            break
        if set(digits) == target_digits:
            solutions.append(from_digits(digits))

print(max(solutions))
