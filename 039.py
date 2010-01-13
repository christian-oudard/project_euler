from utility import isqrt, max_key
from collections import defaultdict
limit = 1000

triangles = defaultdict(set)

for a in range(1, limit):
    for b in range(1, limit):
        c2 = a**2 + b**2
        c = isqrt(c2)
        if c**2 != c2:
            continue

        perimeter = a + b + c
        if perimeter > limit:
            continue
        triangles[perimeter].add(frozenset((a, b, c)))

print(max_key(triangles.items(), key_func=len))
