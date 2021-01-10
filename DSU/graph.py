def findSet(u):
    while u != parent[u]:
        u = parent[u]
    return u

def joinSet(u, v):
    up = findSet(u)
    vp = findSet(v)
    if up != vp:
        parent[up] = vp

def convertToNumb(x):
    return ord(x) - ord('A')

n = int(input())
input()
for q in range(n):
    letter = input()
    numb = convertToNumb(letter)
    parent = [i for i in range(numb + 1)]
    while True:
        try:
            line = input()
            if not line:
                break
            first = convertToNumb(line[0])
            second = convertToNumb(line[1])
            joinSet(first, second)
        except EOFError:
            break
    count = 0
    for i in range(numb + 1):
        if parent[i] == i:
            count += 1
    if q != n - 1:
        print(count)
        print()
    else:
        print(count)