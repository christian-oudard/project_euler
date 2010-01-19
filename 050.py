from utility import primes, is_prime

def prime_sequence_sums(limit):
    prime_list = []
    for p in primes():
        prime_list.append(p)
        if sum(prime_list) >= limit:
            return
        for i in range(len(prime_list)):
            sequence = prime_list[i:]
            if len(sequence) <= 1:
                continue
            s = sum(sequence)
            if is_prime(s):
                yield sequence, s

def best_sequence(limit):
    best = [2]
    best_total = 2
    for sequence, total in prime_sequence_sums(limit):
        if len(sequence) > len(best):
            best = sequence
            best_total = total
    return best_total

print(best_sequence(1000000))
