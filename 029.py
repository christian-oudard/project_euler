MAX_NUM = 100
domain = range(2, MAX_NUM + 1)
numbers = set(a**b for a in domain for b in domain)
print(len(numbers))
