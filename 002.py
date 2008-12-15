def iter_fibonacci(limit):
    a = 0
    b = 1
    yield a
    yield b
    while b <= limit:
        c = a + b
        yield c
        a, b, = b, c

print(sum(f for f in iter_fibonacci(4000000) if f % 2 == 0))
