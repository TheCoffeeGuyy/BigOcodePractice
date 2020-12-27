n, m, k = map(int, input().split())
lakes= []
table = []
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
for _ in range(n):
    table.append(list(input()))

visited = [[False] * 51 for _ in range(51)]

def DFS(sr, sc):
    q = [(sr,sc)]
    visited[sr][sc] = True
    isOcean = False
    temp = []

    while len(q) > 0:
        ur, uc = q.pop()
        temp.append((ur, uc))
        if ur == 0 or uc == 0 or ur == n - 1 or uc == m -1:
            isOcean = True
        for i in range(4):
            u = ur + dx[i]
            c = uc + dy[i]
            if u in range(n) and c in range(m) and table[u][c] == '.' and not visited[u][c]:
                visited[u][c] = True
                q.append((u, c))
    if not isOcean:
        lakes.append(temp)

for i in range(n):
    for j in range(m):
        if not visited[i][j] and table[i][j] == '.':
            DFS(i, j)
blockCells = 0
lakes.sort(key=lambda lake: len(lake))
for i in range(len(lakes) - k):
    blockCells += len(lakes[i])
    for x,y in lakes[i]:
        table[x][y] = '*'
print(blockCells)
for i in range(n):
    print(''.join(table[i]))
