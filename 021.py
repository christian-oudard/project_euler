from utility import proper_divisors

def amicable(a):
    b = sum(proper_divisors(a)) 
    if a == b:
        return False
    a2 = sum(proper_divisors(b))
    return a == a2

print(sum(i for i in range(1, 10000) if amicable(i)))
