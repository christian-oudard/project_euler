#! /usr/bin/env python3

import subprocess
import time

def main():
    total_time = 0.0
    for problem, solution in problems:
        print('%s:' % (problem,), end=' ')
        start = time.time()
        output = subprocess.getoutput('python3 %s.py' % problem)
        finish = time.time()
        print(output)
        if int(output) != solution:
            print('^^^ WRONG')
        run_time = finish - start
        total_time += run_time
        print('{:.3f}s'.format(run_time))
    print('Total Time: {:.3f}s'.format(total_time))

problems = (
    ('001', 233168),
    ('002', 4613732),
    ('003', 6857),
    ('004', 906609),
    ('005', 232792560),
    ('006', 25164150),
    ('007', 104743),
    ('008', 40824),
    ('009', 31875000),
    ('010', 142913828922),
    ('011', 70600674),
    ('012', 76576500),
    ('013', 5537376230),
    ('014', 837799),
    ('015', 137846528820),
    ('016', 1366),
    ('017', 21124),
    ('018', 1074),
    ('019', 171),
    ('020', 648),
    ('021', 31626),
    ('022', 871198282),
    ('023', 4179871),
    ('024', 2783915460),
    ('025', 4782),
    ('026', 983),
    ('027', -59231),
    ('028', 669171001),
    ('029', 9183),
    ('030', 443839),
    ('031', 73682),
    ('032', 45228),
    ('033', 100),
    ('034', 40730),
    ('035', 55),
    ('036', 872187),
    ('037', 748317),
    ('038', 932718654),
    ('039', 840),
    ('040', 210),
    ('041', 7652413),
    ('042', 162),
    ('043', 16695334890),
    ('044', 5482660),
    ('045', 1533776805),
    ('046', 5777),
    ('047', 134043),
    ('048', 9110846700),
    ('049', 296962999629),
    ('050', 997651),
    ('051', 121313),
    ('052', 142857),
    ('053', 4075),
    ('054', 376),
    ('055', 249),
    ('056', 972),
    ('057', 153),
    ('058', 26241),
    ('059', 107359),
    ('067', 7273),
    ('069', 510510),
    ('068', 6531031914842725),
    ('070', 8319823),
    ('071', 428570),
    ('072', 303963552391),
    ('085', 2772),
    ('097', 8739992577),
    ('100', 756872327473),
    ('107', 259679),
    ('234', 1259187438574927161),
)

if __name__ == '__main__':
    main()
