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
    >>> assert (list(search_combinations(200, [200, 100, 50])) ==
    ...         [{200: 1}, {100: 2}, {100: 1, 50: 2}, {50: 4}])
    >>> assert (list(search_combinations(200, [200, 100, 50, 20])) ==
    ...         [{200: 1}, {100: 2}, {100: 1, 50: 2}, {100: 1, 20: 5},
    ...          {50: 4}, {50: 2, 20: 5}, {20: 10}])
    >>> list(search_combinations(200, [200, 100, 50, 20, 10]))
    """
    denominations.sort(reverse=True)
    biggest = denominations[0]

    q, r = divmod(target_value, biggest)
    if r == 0:
        yield {biggest: q}

    if len(denominations) == 1:
        return

    for i in reversed(range(q)):
        if i == 0:
            current = {}
        else:
            current = {biggest: i}
        for solution in search_combinations(
            target_value - valuation(current),
            denominations[1:],
        ):
            solution.update(current)
            yield solution

denominations = [200, 100, 50, 20, 10, 5, 2, 1]
combinations_recursive = list(search_combinations(200, denominations))
print('recursive')
print(len(combinations_recursive))

from copy import copy
def search_iterative(target):
    solutions = []
    combination = {}
    for twopound in range(target // 200 + 1):
        combination[200] = twopound
        for onepound in range(target // 100 + 1):
            combination[100] = onepound
            for fiftypence in range(target // 50 + 1):
                combination[50] = fiftypence
                for twentypence in range(target // 20 + 1):
                    combination[20] = twentypence
                    for tenpence in range(target // 10 + 1):
                        combination[10] = tenpence
                        for fivepence in range(target // 5 + 1):
                            combination[5] = fivepence
                            if valuation(combination) > target:
                                break
                            for twopence in range(target // 2 + 1):
                                combination[2] = twopence
                                value = valuation(combination)
                                if value > target:
                                    break
                                onepence = target - value
                                combination[1] = onepence
                                yield copy(combination)
                                combination[1] = 0
                            combination[2] = 0

combinations_iterative = list(search_iterative(200))
print('iterative')
print(len(combinations_iterative))

combinations_iterative = set(tuple(sorted(c.items())) for c in combinations_iterative)
combinations_recursive = set(tuple(sorted(c.items())) for c in combinations_recursive)

not_in_iterative = []
for cr in combinations_recursive:
    if cr not in combinations_iterative:
        not_in_iterative.append(cr)
print('not in iterative', len(not_in_iterative))

not_in_recursive = []
for ci in combinations_iterative:
    if ci not in combinations_recursive:
        not_in_recursive.append(ci)
print('not in recursive', len(not_in_recursive))

combinations = sorted(combinations_recursive | combinations_iterative)

for c in combinations:
    assert valuation(c) == 200

print(len(combinations))

