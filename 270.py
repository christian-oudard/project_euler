from pprint import pprint
from utility import all_pairs, partition

def square_points(size):
    top = set()
    bottom = set()
    left = set()
    right = set()
    for x in range(size + 1):
        top.add((x, 0))
        bottom.add((x, size))

    for y in range(size + 1):
        left.add((0, y))
        right.add((size, y))

    return top | bottom | left | right

def is_legal_cut(a, b, size):
    ax, ay = a
    bx, by = b
    return not (ax == 0 and bx == 0 or
                ax == size and bx == size or
                ay == 0 and by == 0 or
                ay == size and by == size)

def all_cuts(points, size):
    cuts = set()
    for a, b in all_pairs(points):
        cuts.add(tuple(sorted((a, b))))
    return set(c for c in cuts if is_legal_cut(*c, size=size))


def search_cut_tree(points, size):
    """
    Enumerate the tree of possible cut combinations.

    Recursively cut the square, and continue searching on each half.
    """

    def search(points):
        for a, b in all_cuts(points, size):
            left, right = partition(points, a, b)
            for c in search(left):
                yield c
            yield (a, b)
            for c in search(right):
                yield c

    return list(search(points))

for size in range(8):
    print(str(size).ljust(3), end=' ')
    points = square_points(size)
    print('points', len(points), end=' ')
    #pprint(points)

    cuts = all_cuts(points, size)
    print('cuts', len(cuts), end=' ')
    #pprint(sorted(cuts))

    tree = search_cut_tree(points, size)
    print('tree', len(tree), end=' ')
    #pprint(sorted(tree))

    print()


