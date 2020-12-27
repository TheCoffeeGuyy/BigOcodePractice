INF = 10e9

def Bell(s):
    dist[s] = 0
    for i in range(n - 1):
        for edge in graph:
            u, v, w = edge
            if dist[u] != INF:
                dist[v] = min(dist[v], dist[u] + w)
    
    for i in range(n - 1):
        for edge in graph:
            u, v, w = edge
            if dist[u] != INF and dist[u] + w < dist[v]:
                dist[v] = -INF

while True:
    n, m, q, s = map(int, input().split())
    if n == 0:
        break
    graph = []
    dist = [INF] * (n + 5)
    for i in range(m):
        u, v, w = map(int, input().split())
        graph.append((u,v ,w))
    # Bell algo
    Bell(s)
    # queries    
    for i in range(q):
        f = int(input())
        if dist[f] == -INF:
            print('-Infinity')
        elif dist[f] == INF:
            print('Impossible')
        else:
            print(dist[f])
    
    print()
        
