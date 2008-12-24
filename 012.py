import itertools
from utility import num_divisors

def triangle_numbers():
    t = 1
    n = 1
    while True:
        yield t
        n += 1
        t += n

target = 500
for t in triangle_numbers():
    num = num_divisors(t) 
    if num > target:
        print(t)
        break
