# find the only pythagorean triple whose numbers sum to 1000, and print the
# product of the numbers

from utility import product

def pythagorean_triple_summing_to(n):
    for a in range(1, n // 2):
        for b in range(a, n // 2):
            c = n - a - b # a + b + c sum to n
            if c < b:
                continue # numbers out of order
            if c > a + b:
                continue # cannot make a triangle at all, c is too large
            if a**2 + b**2 == c**2:
                return (a, b, c)

print(product(pythagorean_triple_summing_to(1000)))
