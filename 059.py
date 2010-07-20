import string
import itertools

def crypt(codes, key):
    """
    >>> crypt([65], [42])
    [107]
    """
    crypted = []
    for k, c in zip(itertools.cycle(key), codes):
        crypted.append(k ^ c)
    return crypted

if __name__ == '__main__':
    with open('data/cipher1.txt') as f:
        data = f.read()
    codes = [int(c) for c in data.split(',')]

    def keys():
        letters = string.ascii_lowercase
        for a in letters:
            for b in letters:
                for c in letters:
                    yield (ord(a), ord(b), ord(c))

    for key in keys():
        decrypted = crypt(codes, key)
        decrypted_string = ''.join(chr(c) for c in decrypted)
        if all(c in string.printable for c in decrypted_string):
            if 'the' in decrypted_string and 'and' in decrypted_string:
                print(sum(decrypted))
                break
