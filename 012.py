from utility import up_to, prime_factorization

def triangle_numbers():
    t = 1
    n = 1
    while True:
        yield t
        n += 1
        t += n

def divisors_naive(n):
    for d in range(1, n+1):
        if n % d == 0:
            yield d

def divisors(n):
    pass

import time
start = time.time()
num_divisors_list = []
for t in up_to(1000000, triangle_numbers()):
    num_divisors = sum(1 for i in prime_factorization(t))
    num_divisors_list.append(num_divisors)
end = time.time()
print(max(num_divisors_list))
print('%.3fs' % (end - start))



    
