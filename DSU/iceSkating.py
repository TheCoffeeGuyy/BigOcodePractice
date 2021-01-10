def findSet(u):
    while u != parent[u]:
        u = parent[u]
    return u

def joinSet(u, v):
    up = findSet(u)
    vp = findSet(v)
    if up != vp:
        parent[up] = vp

n = int(input())
x = [0 for i in range(n)]
y = [0 for i in range(n)]
parent = [i for i in range(n)]
for i in range(n):
    x[i], y[i] = map(int, input().split())

for i in range(n):
    for j in range(i + 1, n):
        if x[i] == x[j] or y[i] == y[j]:
            joinSet(i, j)
count = 0
for i in range(n):
    if parent[i] == i:
        count += 1
print(count - 1)   