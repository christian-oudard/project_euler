import os

with open(os.path.join('data', 'names.txt')) as f:
    names = f.read()

names = [n.strip('"') for n in names.split(',')]
names.sort()

def name_score(name):
    return sum(ord(c) - ord('A') + 1 for c in name)

total_score = 0
for index, name in enumerate(names):
    total_score += (index + 1) * name_score(name)
print(total_score)
