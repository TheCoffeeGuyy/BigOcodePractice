while True:
    nm = list(input().split())
    if len(nm) == 1:
        break
    n = int(nm[0])
    m = int(nm[1])
    graph = []
    dist = [-1.0] * (n + 5)
    for i in range(m):
        u, v, w = map(int, input().split())
        graph.append((u,v,w/100))
    # Bell algo
    dist[1] = 1.0
    for i in range(1, n + 1):
        for edge in graph:
            u, v, w = edge
            dist[v] = max(dist[v], dist[u] * w)
            dist[u] = max(dist[u], dist[v] * w)
    print("{:.6f} percent".format(dist[n] * 100))