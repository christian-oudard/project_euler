from fractions import Fraction
import itertools
from utility import digits_of

def sqrt_two_frac_terms():
    frac = Fraction(0, 1)
    while True:
        frac = 1 / (2 + frac)
        yield 1 + frac

count = 0
for term in itertools.islice(sqrt_two_frac_terms(), 1000):
    if len(digits_of(term.numerator)) > len(digits_of(term.denominator)):
        count += 1
print(count)
