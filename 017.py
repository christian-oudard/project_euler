ones = {
    1: 'one',
    2: 'two',
    3: 'three', 
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine',
}

teens = {
    11: 'eleven',
    12: 'twelve',
    13: 'thirteen',
    14: 'fourteen',
    15: 'fifteen',
    16: 'sixteen',
    17: 'seventeen',
    18: 'eighteen',
    19: 'nineteen',
}

tens = {
    10: 'ten',
    20:'twenty',
    30:'thirty',
    40:'forty',
    50:'fifty',
    60:'sixty',
    70:'seventy',
    80:'eighty',
    90:'ninety',
}

hundred = 'hundred'
thousand = 'thousand'
and_ = 'and'

def words(number):
    """
    >>> words(1)
    'one'
    >>> words(11)
    'eleven'
    >>> words(101)
    'one hundred and one'
    >>> words(111)
    'one hundred and eleven'
    """

    if number > 1000 or number < 1:
        raise ValueError
    if number == 1000:
        return [ones[1], thousand]
    result = []

    hundreds_place, number = divmod(number, 100)
    tens_place, ones_place = divmod(number, 10)

    if hundreds_place in ones.keys():
        result.append(ones[hundreds_place])
        result.append(hundred)

    if hundreds_place and (tens_place or ones_place):
        result.append(and_)

    if (10 * tens_place + ones_place) in teens.keys():
        result.append(teens[number])
    else:
        if tens_place in ones.keys():
            result.append(tens[10 * tens_place])
        if ones_place in ones.keys():
            result.append(ones[ones_place])

    return result

letter_count = 0
for i in range(1, 1000 + 1):
    letter_count += sum(len(w) for w in words(i))

print(letter_count)
