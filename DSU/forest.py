def findSet(u):
    while u != parent[u]:
        u = parent[u]
    return u

def joinSet(u, v):
    up = findSet(u)
    vp = findSet(v)
    if up != vp:
        parent[up] = vp
    
test = int(input())
input()

while test > 0:
    p, t = map(int, input().split())
    trees = [set() for i in range(p + 1)]
    parent = [i for i in range(p + 1)]
    while True:
        try:
            line = input()
            if not line:
                break
            person, tree = map(int, line.split())
            trees[person].add(tree)

        except EOFError:
            break
    
    for i in range(1, p + 1):
        for j in range(i + 1, p + 1):
            if trees[i] == trees[j]:
                joinSet(i, j)
    
    count = 0
    for i in range(1, p+1):
        if parent[i] == i:
            count += 1
    print(count)
    test -= 1
    if test > 0:
        print()