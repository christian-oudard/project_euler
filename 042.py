from utility import up_to, figurate_numbers

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

with open('data/words.txt') as f:
    word_data = f.read()

words = [w.strip('"').lower() for w in word_data.split(',')]

t_nums = set(up_to(30 * 26, figurate_numbers(3)))
print(sum(1 for w in words if word_value(w) in t_nums))

