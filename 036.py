def is_palindrome(string):
    """
    >>> is_palindrome('abcde')
    False
    >>> is_palindrome('abcba')
    True
    """
    return string == ''.join(reversed(string))

def gen_double_palindromes(limit):
    for i in range(limit):
        if is_palindrome(str(i)) and \
           is_palindrome(bin(i)[2:]):
            yield i

print(sum(gen_double_palindromes(1000000)))
