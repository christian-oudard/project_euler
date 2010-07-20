from utility import totient

max_ratio = 0
max_n = 0
for n in range(1, 1000000 + 1):
    t = totient(n)
    ratio = n / t
    if ratio > max_ratio:
        max_ratio = ratio
        max_n = n

print(max_n)
