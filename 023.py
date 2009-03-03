from utility import proper_divisors

limit = 28123

def is_abundant(n):
    return sum(proper_divisors(n)) > n

abundant_numbers = [n for n in range(limit) if is_abundant(n)]
abundant_set = set(abundant_numbers)

def find_abundant_pair(target):
    length = len(abundant_numbers)
    for lo in abundant_numbers:
        if lo >= target:
            break
        hi = target - lo
        if hi in abundant_set:
            return (lo, hi)
    return None

print(sum(i for i in range(limit) if not find_abundant_pair(i)))
