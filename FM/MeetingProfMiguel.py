INF = 10e9
MAX_NODES = 30
def FM(dist):
    for k in range(MAX_NODES):
        for i in range(MAX_NODES):
            for j in range(MAX_NODES):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

while True:
    N = int(input())
    if N == 0:
        break
    
    distY = [[0 if i == j else INF for j in range(MAX_NODES)] for i in range(MAX_NODES)] 
    distM = [[0 if i == j else INF for j in range(MAX_NODES)] for i in range(MAX_NODES)] 

    for _ in range(N):
        age, dir, x, y, w = input().split()
        u, v = map(lambda value: ord(value) - ord('A'), (x, y))

        if age == 'Y':
            distY[u][v] = min(distY[u][v], int(w))
            if dir == 'B':
                distY[v][u] = min(distY[v][u], int(w))
        else:
            distM[u][v] = min(distM[u][v], int(w))
            if dir == 'B':
                distM[v][u] = min(distM[v][u], int(w))
        
    s, f = map(lambda value: ord(value) - ord('A'), input().split())
    FM(distM)
    FM(distY)
    result = []
    minDist = INF
    
    for i in range(MAX_NODES):
        dist1 = distY[s][i]
        dist2 = distM[f][i]
        if dist1 != INF and dist2 != INF and dist1 + dist2 <= minDist:
            minDist = dist1 + dist2
            result.append((minDist, i))
    
    if len(result) == 0:
        print('You will never meet.')
    else:
        result.sort()
        print(minDist, end='')
        for res in result:
            if res[0] != minDist:
                break
            print(' ' + chr(res[1] + ord('A')), end='')
        print()