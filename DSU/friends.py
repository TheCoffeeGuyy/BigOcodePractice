def findSet(u):
    while u != parent[u]:
        u = parent[u]
    return u

def unionSet(u, v):
    up = findSet(u)
    vp = findSet(v)
    if up != vp:
        parent[up] = vp
        cnt[vp] += cnt[up]

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    parent = [i for i in range(n + 5)]
    cnt = [1 for i in range(n + 5)]
    for i in range(m):
        u, v = map(int, input().split())
        unionSet(u, v)
    print(max(cnt))