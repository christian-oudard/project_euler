from utility import up_to

def fibonacci():
    a = 0
    b = 1
    yield a
    while True:
        yield b
        a, b = b, a + b

print(sum(f for f in up_to(4000000, fibonacci()) if f % 2 == 0))
