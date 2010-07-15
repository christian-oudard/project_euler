from collections import defaultdict
from utility import primes, is_prime, all_pairs

def catenate(a, b):
    """
    >>> catenate(1, 234)
    1234
    """
    return int(str(a) + str(b))

def iter_pairs(iterable):
    """
    Iterate pairs of a potentially infinite iterable.

    >>> import itertools
    >>> list(itertools.islice(iter_pairs(itertools.count()), 6))
    [(1, 0), (2, 0), (2, 1), (3, 0), (3, 1), (3, 2)]
    """
    seen = []
    for a in iterable:
        for b in seen:
            yield (a, b)
        seen.append(a)

def is_prime_pair(a, b):
    return (is_prime(catenate(a, b)) and
            is_prime(catenate(b, a)))

def test_set(primes):
    return all(is_prime_pair(a, b) for a, b in all_pairs(primes))

# Start with a list of primes, and a set of all two-way pairs between those
# primes, and a list of groups of mutually paired primes.
# Add a prime. Check that prime against all existing primes for pairs, and add
# them to the pair set. Check primes that it pairs with for being in an
# existing group, if so, the group has grown.

# The set of paired primes creates an undirected graph. Find a fully connected subgraph of size 5.

def find_groups():
    minimum_size = 3

    pair_graph = defaultdict(set)
    seen_primes = []
    for hi in primes():
        if hi > 70: return # DEBUG
        for lo in seen_primes:
            if is_prime_pair(hi, lo):
                pair_graph[lo].add(hi)
                pair_graph[hi].add(lo)
        seen_primes.append(hi)

        # We now have a complete pair graph up to hi.
        # Check hi and its neighbors for containing a fully connected subgraph
        # of the prerequisite size.
        neighbors = pair_graph[hi]
        group = {hi}
        for neighbor in neighbors:
            connections =

        while stack:
            current = stack.pop()
            neighbors = pair_graph[current]
            group &= neighbors
            print(group)
            if hi not in group:
                break
            if len(group) < minimum_size:
                break


        # Find new groups of three.

        #for a, b in all_pairs(pair_graph[hi]):
        #    if b in pair_graph[a]:
        #        group = frozenset((hi, a, b))
        #        #groups.add(group)
        #        print(sum(group), *sorted(group, reverse=True))

    print(pair_graph)

if __name__ == '__main__':
    #print(test_set([3, 7, 109, 673]))

    find_groups()


