import itertools
from utility import digits_of, from_digits, is_prime

# We only need to search 4 and 7 digit pandigital numbers for primality. For
# other sizes of numbers, their digital roots show that they are always
# divisible by 3 (http://en.wikipedia.org/wiki/Digital_root).
# 1+2+3+4+5+6+7+8+9 = 45, 4+5 = 9
# 1+2+3+4+5+6+7+8 = 36, 3+6 = 9
# etc.

def digit_permutations(n):
    for digits in itertools.permutations(digits_of(n)):
        yield from_digits(digits)

print(max(p for p in digit_permutations(1234567) if is_prime(p)))
