dx = [0, 0, 1, 1, 1, -1, -1, -1]
dy = [1, -1, 0, 1, -1, 0, 1, -1]
# query = int(input())
n, m = map(int, input().split())

table = [[] for _ in range(105)]
visited = [[False] * 103 for i in range(103)]
ALL_IZZ_WELL = 'ALLIZZWELL'

for i in range(n):
    table[i] = list(input())

def DFS(sr, sc):
    q = [(sr, sc)]
    visited[sr][sc] = True
    count = 1 
    while len(q) > 0:
        ur, uc = q.pop()
        for i in range(8):
            r = ur + dx[i]
            c = uc + dy[i]
            if count == len(ALL_IZZ_WELL):
                return True
            if r in range(n) and c in range(m) and not visited[r][c] and table[r][c] == ALL_IZZ_WELL[count]:
                print(r, c)
                visited[r][c] == True
                count += 1
                q.append((r, c))
                visited[r][c] == False

                
    return False

for i in range(n):
    for j in range(m):
        if table[i][j] == 'A':
            if DFS(i,j):
                print('YES')
            else:
                print('NO')