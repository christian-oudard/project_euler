import subprocess
import time

def main():
    for problem, solution in problems:
        print('%s:' % (problem,), end=' ')
        start = time.time()
        output = subprocess.getoutput('python3 %s.py' % problem)
        finish = time.time()
        print(output)
        if int(output) != solution:
            print('^^^ WRONG')
        print('%.3fs' % (finish - start,))

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
    ('048', 9110846700),
    ('067', 7273),
)

if __name__ == '__main__':
    main()
