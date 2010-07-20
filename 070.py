from utility import primes, digits_of, up_to

# In order to maximize the totient, we need to look for "sharp" numbers, having
# few prime factors, with those factors being large.

limit = 10**7

solutions = []
seen_primes = []
for a in up_to(limit // 2, primes()):
    for b in seen_primes:
        n = a * b
        if n > limit:
            break
        t = n
        t -= t // a
        if a != b:
            t -= t // b
        if sorted(digits_of(n)) == sorted(digits_of(t)):
            solutions.append((n, n / t))
    seen_primes.append(a)

solutions.sort(key=lambda x: x[1])
print(min(solutions, key=lambda x: x[1])[0])
