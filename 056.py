from utility import digits_of

print(max(sum(digits_of(a**b)) for a in range(1, 100) for b in range(1, 100)))
