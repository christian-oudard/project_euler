import subprocess
import time

def main():
    for problem, solution in problems:
        start = time.time()
        output = subprocess.getoutput('python3 %s.py' % problem)
        finish = time.time()
        print('%s: %s' % (problem, output))
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
)

if __name__ == '__main__':
    main()
