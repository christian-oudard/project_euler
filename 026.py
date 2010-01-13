from utility import max_key

def rep_digits(n, base=10):
    """
    Find the repeating digits of the decimal expansion of 1/n.

    >>> rep_digits(2)
    []
    >>> rep_digits(3)
    [3]
    >>> rep_digits(4)
    []
    >>> rep_digits(5)
    []
    >>> rep_digits(6)
    [6]
    >>> rep_digits(7)
    [1, 4, 2, 8, 5, 7]
    >>> rep_digits(8)
    []
    >>> rep_digits(9)
    [1]
    >>> rep_digits(10)
    []
    """
    digit_list = []
    seen_pairs = set()
    order = base
    while True:
        digit, rem = pair = divmod(order, n)
        if pair == (0, 0):
            return [] # Exact division, no repeating digits.
        # Check if we've seen this digit and remainder before. If so, we've
        # found the repetition, so return.
        if pair in seen_pairs:
            i = digit_list.index(pair)
            return [d for d, r in digit_list[i:]]
        # Mark the digit as seen, and go to the next higher order.
        seen_pairs.add(pair)
        digit_list.append(pair)
        order = rem * base

print(max_key((n, len(rep_digits(n))) for n in range(1, 1000)))
