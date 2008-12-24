from utility import lcm

limit = 20
answer = 1
for i in range(2, limit):
    answer = lcm(answer, i)
print(answer)
