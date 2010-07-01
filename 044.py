from utility import figurate_numbers

def search_pentagonal_sum_difference():
    # Find pentagonal numbers a and b such that a + b and a - b are also pentagonal.
    # Treat c = a + b as fundamental, and derive b and a - b from it
    # b = c - a
    # (a - b) = a - (c - a) = 2 * a - c
    seen = set()
    seen_list = []
    for c in figurate_numbers(5):
        for a in seen_list:
            b = c - a
            a_minus_b = 2 * a - c
            #assert a_minus_b == a - b
            #assert a + b == c
            if b in seen and a_minus_b in seen:
                return a_minus_b
        seen.add(c)
        seen_list.append(c)

print(search_pentagonal_sum_difference())
