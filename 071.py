#Consider the fraction, n/d, where n and d are positive integers. If nd and HCF(n,d)=1, it is called a reduced proper fraction.
#
#If we list the set of reduced proper fractions for d  8 in ascending order of size, we get:
#
#1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 5/8, 2/3, 5/7, 3/4, 4/5, 5/6, 6/7, 7/8
#
#It can be seen that 2/5 is the fraction immediately to the left of 3/7.
#
#By listing the set of reduced proper fractions for d  1,000,000 in ascending order of size, find the numerator of the fraction immediately to the left of 3/7.

from fractions import Fraction
from utility import divide_ceil

def f_naive(target, max_denominator):
    fracs = set()
    for d in range(1, max_denominator + 1):
        for n in range(1, d):
            fracs.add(Fraction(n, d))

    fracs = sorted(fracs)
    i = fracs.index(target)
    return fracs[i-1]

def find_nearest_fraction_neighbor_slow(target, max_denominator):
    best = 0
    for d in range(1, max_denominator + 1):
        n_start = 1
        if best:
            n_start = best.numerator
        for n in range(n_start, d):
            f = Fraction(n, d)
            if best < f < target:
                best = f
            if f >= target:
                break
    return best

def find_nearest_fraction_neighbor(target, max_denominator):
    best = 0
    start_d = max(1, max_denominator - target.denominator) # Probably an invalid optimization. What is the real bound on this?
    for d in range(start_d, max_denominator + 1):
        # Calculate n so that n / d is greater than or equal to the target,
        # and (n - 1) / d is strictly less than the target.
        n = divide_ceil(target.numerator * d, target.denominator)
        f = Fraction(n - 1, d)
        assert f < target
        if f > best:
            best = f
    return best

def test():
    target = Fraction(3, 7)
    for max_denominator in range(7, 1000):
        #assert (f_naive(target, max_denominator) ==
        assert (find_nearest_fraction_neighbor_slow(target, max_denominator) ==
                find_nearest_fraction_neighbor(target, max_denominator)), max_denominator

if __name__ == '__main__':
    #test()
    print(find_nearest_fraction_neighbor(Fraction(3, 7), 1000000).numerator)
