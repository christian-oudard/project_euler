from utility import ncr

count = 0
for n in range(1, 100 + 1):
    for r in range(1, n + 1):
        if ncr(n, r) > 1000000:
            count += 1
print(count)
