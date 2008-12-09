import subprocess

def main():
    for problem, solution in problems:
        output = subprocess.getoutput('python3 %s.py' % problem)
        print('%s: %s' % (problem, output))
        if int(output) != solution:
            print('^^^ WRONG')

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
)

if __name__ == '__main__':
    main()
