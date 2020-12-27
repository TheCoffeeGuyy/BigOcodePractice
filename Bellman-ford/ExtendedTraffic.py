T = int(input())
INF = 10e9

def Bell(s):
    dist[s] = 0
    for i in range(n -1):
        for edge in graph:
            u = edge[0]
            v = edge[1]
            w = edge[2]
            if dist[u] != INF:
                dist[v] = min(dist[v], dist[u] + w)

for t in range(1, T + 1):
    input()
    graph = []
    n = int(input())
    dist = [INF] * (n + 5)
    arrayN = [0] + list(map(int, input().split()))
    m = int(input())
    for i in range( m ):
        u, v = map(int, input().split())
        graph.append((u, v, (arrayN[v] - arrayN[u]) ** 3))
    queries = int(input())
    Bell(1)
    print('Case {}:'.format(t))
    for i in range(queries):
        q = int(input())
        if dist[q] != INF and dist[q] >= 3:
            print(dist[q])
        else:
            print('?')
