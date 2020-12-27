import sys
sys.setrecursionlimit(10000000)
dx = [0, 0, 1, 1, 1, -1, -1, -1]
dy = [1, -1, 0, 1, -1, 0, 1, -1]
case = 0

def DFS(sr,sc):
    if dist[sr][sc]:
        return dist[sr][sc]
    maxPath = 0
    for i in range(8):
        r = sr + dx[i]
        c = sc + dy[i]
        if r in range(n) and c in range(m) and ord(table[sr][sc]) + 1 == ord(table[r][c]): 
            maxPath = max(maxPath, DFS(r, c))
    dist[sr][sc] = maxPath + 1
    return dist[sr][sc]

while True:
    case += 1
    n, m = map(int, input().split())
    if n ==0 and m ==0:
        break
    table = []
    dist = [[0] * 50 for i in range(n)]
    for i in range(n):
        table.append(input())
    result = 0
    for i in range(n):
        for j in range(m):
            if table[i][j] == 'A':
                result = max(DFS(i, j), result)
    print('Case {}: {}'.format(case, result))
