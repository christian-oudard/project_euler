from collections import Counter

JACK = 11
QUEEN = 12
KING = 13
ACE = 14

def score_hand(hand):
    """
    Score a particular hand of cards according to poker rules.

    Returns a tuple, (hand rank, high card, next highest card, ...)
    Scores can be compared by direct comparison of the returned tuples.

    The hand ranks and indices are as follows:

    0: High Card: Highest value card.
    >>> score_hand([(3, 'C'), (5, 'D'), (ACE, 'C'), (9, 'C'), (KING, 'D')])
    (0, 14, 13, 9, 5, 3)

    1: One Pair: Two cards of the same value.
    >>> score_hand([(5, 'C'), (5, 'D'), (ACE, 'C'), (9, 'C'), (KING, 'D')])
    (1, 5, 5, 14, 13, 9)

    2: Two Pair: Two different pairs.
    >>> score_hand([(3, 'C'), (3, 'D'), (10, 'H'), (10, 'C'), (ACE, 'S')])
    (2, 10, 10, 3, 3, 14)
    >>> score_hand([(5, 'C'), (5, 'D'), (ACE, 'C'), (9, 'C'), (ACE, 'D')])
    (2, 14, 14, 5, 5, 9)

    3: Three of a Kind: Three cards of the same value.
    >>> score_hand([(3, 'C'), (3, 'D'), (3, 'H'), (10, 'C'), (ACE, 'S')])
    (3, 3, 3, 3, 14, 10)

    4: Straight: All cards are consecutive values.
    >>> score_hand([(2, 'H'), (3, 'D'), (4, 'D'), (5, 'C'), (6, 'H')])
    (4, 6, 5, 4, 3, 2)

    5: Flush: All cards of the same suit.
    >>> score_hand([(2, 'S'), (8, 'S'), (4, 'S'), (KING, 'S'), (6, 'S')])
    (5, 13, 8, 6, 4, 2)

    6: Full House: Three of a kind and a pair.
    >>> score_hand([(3, 'C'), (3, 'D'), (3, 'H'), (10, 'C'), (10, 'S')])
    (6, 3, 3, 3, 10, 10)

    7: Four of a Kind: Four cards of the same value.
    >>> score_hand([(8, 'C'), (8, 'D'), (8, 'H'), (8, 'S'), (ACE, 'S')])
    (7, 8, 8, 8, 8, 14)

    8: Straight Flush: All cards are consecutive values of same suit.
    >>> score_hand([(2, 'H'), (3, 'H'), (4, 'H'), (5, 'H'), (6, 'H')])
    (8, 6, 5, 4, 3, 2)
    """
    values = [v for v, s in hand]
    suits = [s for v, s in hand]

    # Determine straight and flush status.
    is_straight = sorted(values) == list(range(min(values), max(values) + 1))
    is_flush = len(set(suits)) == 1

    # Find multiple values.
    counter = Counter(values)
    counts = sorted(c for c in counter.values() if c >= 2)

    # Determine rank.
    if is_straight and is_flush:
        rank = 8 # straight flush
    elif counts == [4]:
        rank = 7 # four of a kind
    elif counts == [2, 3]:
        rank = 6 # full house
    elif is_flush:
        rank = 5 # flush
    elif is_straight:
        rank = 4 # straight
    elif counts == [3]:
        rank = 3 # three of a kind
    elif counts == [2, 2]:
        rank = 2 # two pair
    elif counts == [2]:
        rank = 1 # one pair
    else:
        rank = 0 # high card

    # Order the score by frequency, then value.
    values.sort(key=lambda x: (counter[x], x), reverse=True)
    return tuple([rank] + values)


if __name__ == '__main__':
    value_codes = {
        'T': 10,
        'J': JACK,
        'Q': QUEEN,
        'K': KING,
        'A': ACE,
    }
    for i in range(2, 9 + 1):
        value_codes[str(i)] = i
    def parse_card(s):
        assert s[1] in ('C', 'D', 'H', 'S')
        return value_codes[s[0]], s[1]

    #from textwrap import dedent
    #test_data = dedent('''
    #    5H 5C 6S 7S KD 2C 3S 8S 8D TD
    #    5D 8C 9S JS AC 2C 5C 7D 8S QH
    #    2D 9C AS AH AC 3D 6D 7D TD QD
    #    4D 6S 9H QH QC 3D 6D 7H QD QS
    #    2H 2D 4C 4D 4S 3C 3D 3S 9S 9D
    #'''.strip())

    p1_wins = 0
    with open('data/poker.txt') as f:
        for line in f:
            cards = [parse_card(c) for c in line.split()]
            p1_hand = cards[0:5]
            p2_hand = cards[5:10]
            if score_hand(p1_hand) > score_hand(p2_hand):
                p1_wins += 1
    print(p1_wins)
