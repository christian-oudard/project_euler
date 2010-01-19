from fractions import Fraction
from utility import digits_of, from_digits, product

def cancel_unorthodox(numerator, denominator):
    """
    >>> cancel_unorthodox(49, 98)
    (4, 8)
    >>> cancel_unorthodox(499, 998)
    (4, 8)
    >>> cancel_unorthodox(11, 12)
    (1, 2)
    """
    n_digits = digits_of(numerator)
    d_digits = digits_of(denominator)
    matching_digits = [d for d in n_digits if d in d_digits]
    for m in matching_digits:
        if m in n_digits and m in d_digits:
            n_digits.remove(m)
            d_digits.remove(m)
    return from_digits(n_digits), from_digits(d_digits)

two_digit_nums = [i for i in range(10, 100)
                  if 0 not in digits_of(i)]
unorthodox_numbers = []
for n in two_digit_nums:
    for d in two_digit_nums:
        f = Fraction(n, d)
        if f >= 1:
            continue
        n2, d2 = cancel_unorthodox(n, d)
        if d2 == 0:
            continue
        if (n, d) == (n2, d2):
            continue
        f2 = Fraction(n2, d2)
        if f == f2:
            unorthodox_numbers.append(f2)

print(product(unorthodox_numbers).denominator)
