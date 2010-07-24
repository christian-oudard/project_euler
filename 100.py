import math

one_plus_sqrt_two = 1 + math.sqrt(2)
magic_ratio = 5.828427124746
def search_ratio():
    a, b, c = 3, 1, 4
    while True:
        yield a, b, c
        b = int(b * magic_ratio) + 1
        a = int(b * one_plus_sqrt_two)
        if a % 2 != 1:
            a += 1
        c = a + b
        assert (a * (a-1)) * 2 == (c * (c-1))

for a, b, c in search_ratio():
    if c > 10**12:
        break
print(a)
