from utility import digits_of, isqrt

# The maximum value of a is 99, because 99 * 100 = 9900, is the largest
# almost-square product with 9 or fewer digits.
# Since order doesn't matter for products, we define b to be greater than a.
# The maximum value for b is 9999, because 1 * 9999 = 9999 is the product with
# the largest value of b having 9 or fewer digits.

all_digits = list(range(1, 9 + 1))
solutions = []
for a in range(1, 100):
    for b in range(a + 1, 10000):
        c = a * b
        digits = digits_of(a) + digits_of(b) + digits_of(c)
        if len(digits) < 9:
            continue
        if len(digits) > 9:
            break
        assert len(digits) == 9
        if sorted(digits) == all_digits:
            solutions.append(c)

print(sum(set(solutions)))
