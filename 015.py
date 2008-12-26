# calculating the whole recursion tree, but with memoization
def f(x, y, _memo={}):
    if y > x:
        x, y = y, x
    cached = _memo.get((x, y))
    if cached:
        return cached
    if y == 0:
        return 1

    result = f(x, y-1) + f(x-1, y)
    _memo[(x, y)] = result
    return result

# direct calculation
from math import factorial
def f(x, y):
    return factorial(x + y) // (factorial(x) * factorial(y))

print(f(20, 20))
