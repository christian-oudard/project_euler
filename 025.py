def fibonacci():
    """
    >>> from itertools import islice
    >>> list(islice(fibonacci(), 10))
    [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
    """
    a = 0
    b = 1
    yield a
    while True:
        yield b
        a, b = b, a + b

digits = 1000
limit = 10**(digits - 1)
for i, f in enumerate(fibonacci()):
    if f >= limit:
        break
print(i)
