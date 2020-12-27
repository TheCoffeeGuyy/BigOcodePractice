import queue
dx = [0,0,1,-1]
dy = [1,-1,0,0]
n, m = map(int, input().split())
MAX = 255
backYard = [None] * MAX
sheepsAlive = 0
wolvesAlive = 0

for i in range(n):
    backYard[i] = list(input())

def BFS(sr, sc):
    global sheepsAlive, wolvesAlive
    q = queue.Queue()
    q.put((sr, sc))
    sheeps = wolves = 0
    canEscape = False
    if backYard[sr][sc] == 'k':
        sheeps +=1
    if backYard[sr][sc] == 'v':
        wolves +=1
    backYard[sr][sc] = '#'
    while not q.empty():
        ur, uc = q.get()
        for i in range(4):
            r = ur + dx[i]
            c = uc + dy[i]
            if not (r in range(n) and c in range(m)):
                canEscape = True
                continue
            if backYard[r][c] != '#':
                if backYard[r][c] == 'k':
                    sheeps +=1
                if backYard[r][c] == 'v':
                    wolves +=1
                q.put((r,c))
                backYard[r][c] = '#'

    if canEscape:
        sheepsAlive += sheeps
        wolvesAlive += wolves
    else:
        if sheeps > wolves:
            sheepsAlive += sheeps
        else:
            wolvesAlive += wolves

for i in range(n):
    for j in range(m):
        if backYard[i][j] != '#':
            BFS(i, j)

print(sheepsAlive, wolvesAlive)