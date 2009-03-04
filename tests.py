#! /usr/bin/python3

from imp import reload
import unittest
import itertools
import utility

class PrimesTestCase(unittest.TestCase):
    def setUp(self):
        reload(utility)

    def testCacheInit(self):
        self.assertEqual(len(utility._primes), 1)
        self.assertEqual(len(utility._composites), 1)

    def testCaching(self):
        from utility import primes
        p1 = list(itertools.islice(primes(), 100))
        calcs = utility._p_calcs
        p2 = list(itertools.islice(primes(), 100))
        self.assertEqual(calcs, utility._p_calcs)
        self.assertEqual(p1, p2)

    def testParallelIteration(self):
        from utility import primes
        p1, p2 = primes(), primes()
        self.assertEqual([next(p1) for i in range(3)], [2, 3, 5])
        self.assertEqual([next(p2) for i in range(6)], [2, 3, 5, 7, 11, 13])
        self.assertEqual([next(p1) for i in range(3)], [7, 11, 13])
        self.assertEqual(utility._p_calcs, 5)

    def testZip(self):
        from utility import primes
        zipped_primes = list(zip(primes(), itertools.islice(primes(), 1, 5)))
        self.assertEqual(zipped_primes, [(2, 3), (3, 5), (5, 7), (7, 11)])

if __name__ == '__main__':
    unittest.main()
