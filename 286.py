#XXX Wrong, not accounting for making 20 points.
def f(q):
    probability = 1
    for x in range(1, 50 + 1):
        probability *= (1 - x / q)
    return probability

#XXX Awful solve function, convergence was reversed hackishly because it's buggy.
def solve(f, target, lower, upper, precision=10):
    lower_value = f(lower)
    upper_value = f(upper)
    assert lower_value < target < upper_value
    for i in range(100):
        middle = (upper + lower) / 2
        middle_value = f(middle)
        if middle_value < target:
            lower = middle
        else:
            upper = middle
    return middle

v = solve(f, target=0.02, lower=100, upper=1000, precision=10)

print('{:.10f}'.format(v))
