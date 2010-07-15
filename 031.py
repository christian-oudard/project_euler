# coding: utf8
#In England the currency is made up of pound, £, and pence, p, and there are eight coins in general circulation:
#
#1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).
#It is possible to make £2 in the following way:
#
#1x£1 + 1x50p + 2x20p + 1x5p + 1x2p + 3x1p
#How many different ways can £2 be made using any number of coins?

def valuation(values):
    try:
        values = values.items()
    except AttributeError:
        pass
    return sum(value * count for value, count in values)

def search_combinations(target_value, denominations):
    """
    >>> list(search_combinations(200, [200]))
    [{200: 1}]
    >>> list(search_combinations(200, [100]))
    [{100: 2}]
    >>> list(search_combinations(200, [200, 100]))
    [{200: 1}, {100: 2}]
    >>> list(search_combinations(200, [100, 200]))
    [{200: 1}, {100: 2}]
    >>> assert (list(search_combinations(200, [200, 100, 50])) == [
    ...     {200: 1}, {100: 2}, {100: 1, 50: 2}, {50: 4}])
    >>> assert (list(search_combinations(200, [200, 100, 50, 20])) == [
    ...     {200: 1}, {100: 2}, {100: 1, 50: 2}, {100: 1, 20: 5},
    ...     {50: 4}, {50: 2, 20: 5}, {20: 10}])
    >>> assert (list(search_combinations(5, [2, 1])) == [
    ...     {2: 2, 1: 1}, {2: 1, 1: 3}, {1: 5}])
    """
    denominations.sort(reverse=True)
    return _search_combinations(target_value, denominations)

def _search_combinations(target_value, denominations):
    if not denominations:
        return

    biggest = denominations[0]

    for i in reversed(range(target_value // biggest + 1)):
        current = {biggest: i} if i > 0 else {}
        current_value = biggest * i

        if current_value == target_value:
            yield current
            continue

        for solution in _search_combinations(
            target_value - current_value,
            denominations[1:],
        ):
            solution.update(current)
            yield solution

denominations = [200, 100, 50, 20, 10, 5, 2, 1]
print(len(list(search_combinations(200, denominations))))
