from utility import is_prime, prime_factorization

def main():
	limit = 20
	factorization_dicts = [frequency_count(prime_factorization(n)) for n in range(2, limit)]
	answer = product(flatten_frequencies(merge_frequency_counts(factorization_dicts)))
	print answer
	print 'pass' if is_divisible_up_to_limit(answer, limit) else 'fail'

def is_divisible_up_to_limit(n, limit):
	if n < limit:
		return False
	for i in range(2, limit+1):
		if n % i != 0:
			#print 'fails at %d mod %d' % (n, i)
			return False
	return True	

def frequency_count(l):
	frequencies = {}
	for i in l:
		if i not in frequencies:
			frequencies[i] = 1
		else:
			frequencies[i] += 1
	return frequencies

def flatten_frequencies(frequency_dict):
	frequency_list = []
	for key, count in frequency_dict.items():
		frequency_list.extend([key] * count)
	return frequency_list

def merge_frequency_counts(frequency_dicts):
	""" Takes a list of frequency dictionaries, and merges them.

	The final dictionary returned contains the maximum of each entry
	across the input dictionaries.
	"""
	master_frequency_counts = {}
	for fd in frequency_dicts:
		for key, count in fd.items():
			if key not in master_frequency_counts:
				master_frequency_counts[key] = [count]
			else:
				master_frequency_counts[key].append(count)
	max_frequency_counts = {}
	for key, fl in master_frequency_counts.items():
		max_frequency_counts[key] = max(fl)
	return max_frequency_counts

def product(l):
	product = 1
	for n in l:
		product *= n
	return product

if __name__ == '__main__':
	main()
