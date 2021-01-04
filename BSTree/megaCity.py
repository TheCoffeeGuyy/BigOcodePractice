import math
n, s = map(int, input().split())
radius = []
dictionary = dict()
for i in range(n):
    x, y, population = map(int, input().split())
    r = x * x + y * y
    if r in dictionary:
        dictionary[r] += population
    else:
        dictionary[r] = population
        radius.append(r)

radius.sort()
for x in radius:
    s += dictionary[x]
    if s >= 1e6:
        print(math.sqrt(x))
        exit()
print(-1)


