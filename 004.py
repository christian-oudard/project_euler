# find the largest palindrome that is the product of two three-digit numbers

# some improvements over brute force:
# the number is of the form abccba, or
# 100000*a + 10000*b + 1000*c + 100*c + 10*b + c
# = 100001*a + 10010*b + 1001*c
# = 11 * (9091*a + 910*b + 11*c)
# so it must be evenly divisible by 11, and so must at least one of its factors.

def is_palindrome(num):
    s = str(num)
    return s == ''.join(reversed(s))

results = []
for a in range(900, 1000):
    for b in range(902, 1000, 11): # go up by 11s
        product = a * b
        if is_palindrome(product):
            results.append(product)

print(max(results))
