MAX = 100
INF = 10e9

def printPath(s,t):
    b = []
    while s != t:
        b.append(t)
        t = path[s][t]
    b.append(s)
    for i in range(len(b) - 1, -1, -1):
        print(b[i], end=' ' if i > 0 else '\n')

def FM(graph, dist):
    for i in range(V):
        for j in range(V):
            dist[i][j] = graph[i][j]
            if graph[i][j] != INF and j != i:
                path[i][j] = i
            else :
                path[i][j] = -1
    
    for k in range(V):
        for i in range(V):
            for j in range(V):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    path[i][j] = path[k][j]
    
    for i in range(V):
        if dist[i][i] < 0:
            return False
    
    return True
    
 