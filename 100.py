#15 6
#(15 / 21) * (14 / 20)
#= (15 * 14) / (20 * 21)
#= (5 * 3 * 7 * 2) / (5 * 2 * 2 * 7 * 3)
#
#85 35
#85 / 120 * 84 / 119
#= (85 * 84) / (120 * 119)
#= (5 * 17 * 2 * 2 * 3 * 7) / (2 * 2 * 2 * 3 * 5 * 7 * 17)
#a
#c = a + b
#a / c * a-1 / c-1 = 1/2
#(a * (a-1)) / (c * c-1) = 1/2
#
#2 * c * (c-1) = a * (a-1)
#
#2 * (c**2 - c) = a**2 - a
#
#15 21
#
#a / c > sqrt(2) / 2
#a-1 / c-1 < sqrt(2) / 2

import itertools
import math
from fractions import Fraction

sqrt_two = math.sqrt(2)
half_sqrt_two = math.sqrt(.5)
one_plus_sqrt_two = 1 + math.sqrt(2)

def search(start, even_odd, mult_four):
    while (start+1) % 4 != mult_four:
        start += 1
    for a in itertools.count(start, 4):
        c = int(a * sqrt_two)
        if c % 2 != even_odd:
            continue
        b = c - a
        if (a * (a-1)) * 2 == (c * (c-1)):
            yield (a, b, c, (a+1) % 4 == 0)

_magic_ratio = 5.828427124746
def search_ratio():
    a, b, c = 3, 1, 4
    while True:
        yield a, b, c
        b = int(b * _magic_ratio) + 1
        a = int(b * one_plus_sqrt_two)
        if a % 2 != 1:
            a += 1
        c = a + b
        #assert (a * (a-1)) * 2 == (c * (c-1))

for a, b, c in search_ratio():
    if c > 10**12:
        break
print(a)

#print(search(2))
#print(search(4))
#print(search(16))
#print(search(86))
#print(search(494))
#print(search(2872))
#
#(a, b, c, c even/odd, a+1 mult of 4)
even = 0
odd = 1
results = [
    (3, 1, 4, even, True),
    (15, 6, 21, odd, True),
    (85, 35, 120, even, False),
    (493, 204, 697, odd, False),
    (2871, 1189, 4060, even, True),
    (16731, 6930, 23661, odd, True),
    (97513, 40391, 137904, even, False),
    (568345, 235416, 803761, odd, False),
    (3312555, 1372105, 4684660, even, True),
    (19306983, 7997214, 27304197, odd, True),
]

#ratios_a = []
#ratios_b = []
#ratios_c = []
#prev = None
#for a, b, c, _, _ in results:
#    print('a / b', a / b)
#    print('b / c', b / c)


#    if prev:
#        pa, pb, pc = prev
#        ratios_a.append(a / pa)
#        ratios_b.append(b / pb)
#        ratios_c.append(c / pc)
#    prev = a, b, c
#
#for ratios in ratios_a, ratios_b, ratios_c:
#    print('-'*8)
#    prev = None
#    for r in ratios:
#        if prev:
#            print(repr(r), r - prev)
#        prev = r
##for result in search(2, even_odd=even, mult_four=False):
##    print(result)
##    break
#a = ratios_a[-1]
#b = ratios_c[-1]
