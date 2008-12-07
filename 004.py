def is_palindrome(num):
	s = str(num)
	return s == str_reverse(s)

def str_reverse(s):
	return ''.join(reversed(s))

def iter_all_3digit_pairs():
	three_digit_numbers = list(range(100, 1000))
	for a in three_digit_numbers:
		for b in three_digit_numbers:
			yield a, b

l = []
d = {}
for a, b in iter_all_3digit_pairs():
	product = a * b
	if is_palindrome(product):
		l.append(product)
		d[product] = (a, b)
m = max(l)
a, b = d[m]
assert(a * b == m)
print('%i * %i = %i' % (a, b, m))
