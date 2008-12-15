from collections import defaultdict
from utility import is_prime, prime_factorization, frequency_count, product

def main():
    limit = 20
    factorization_dicts = [frequency_count(prime_factorization(n)) for n in range(2, limit)]
    answer = product(flatten_frequencies(merge_frequency_counts(factorization_dicts)))
    print(answer)

def flatten_frequencies(frequency_dict):
    frequency_list = []
    for key, count in list(frequency_dict.items()):
        frequency_list.extend([key] * count)
    return frequency_list

def merge_frequency_counts(frequency_dicts):
    """ Takes a list of frequency dictionaries, and merges them.

    The final dictionary returned contains the maximum of each entry
    across the input dictionaries.
    """
    master_frequency_counts = defaultdict(list)
    for fd in frequency_dicts:
        for key, count in fd.items():
            master_frequency_counts[key].append(count)
    max_frequency_counts = {}
    for key, fl in master_frequency_counts.items():
        max_frequency_counts[key] = max(fl)
    return max_frequency_counts

if __name__ == '__main__':
    main()
