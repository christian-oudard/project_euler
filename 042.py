from utility import up_to

def letter_value(c):
    """
    >>> [letter_value(c) for c in 'abcdefghijklmnopqrstuvwxyz']
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]
    """
    c = c.lower()
    return ord(c) - ord('a') + 1

def word_value(word):
    """
    >>> word_value('sky')
    55
    """
    return sum(letter_value(c) for c in word)

def triangle_numbers():
    """
    >>> list(up_to(100, triangle_numbers()))
    [1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 78, 91]
    """
    n = 0
    d = 1
    while True:
        n += d
        d += 1
        yield n

with open('data/words.txt') as f:
    word_data = f.read()

words = [w.strip('"').lower() for w in word_data.split(',')]

t_nums = set(up_to(30 * 26, triangle_numbers()))
print(sum(1 for w in words if word_value(w) in t_nums))

