energy = [0] * 105
INF = 10e9
import queue

def hasPath(s,f):
    visited = [False] * (n + 1)
    q = queue.Queue()
    visited[s] = True
    q.put(s)
    while not q.empty():
        u = q.get()
        for edge in graph:
            if u == edge[0]:
                v = edge[1]
                if not visited[v]:
                    visited[v] = True
                    q.put(v)
                if v == f:
                    return True
    return False

def Bell(s, f):
    dist = [-INF] * (n + 1)
    dist[1] = 100
    for i in range(1, n + 1):
        for edge in graph:
            source = edge[0]
            target = edge[1]
            if dist[source] > 0:
                dist[target] = max(dist[target], dist[source] + energy[target])
    
    for edge in graph:
        source = edge[0]
        target = edge[1]
        if dist[source] > 0 and dist[source] + energy[target] > dist[target] and hasPath(source, f):
            return True
    return dist[f] > 0


while True:
    n = int(input())
    if n == -1:
        break
    graph = []
    for i in range(1, n + 1):
        line = list(map(int, input().split()))
        energy[i] = line[0]
        if line[1] != 0:
            for j in range(line[1]):
                graph.append((i, line[2 + j]))
    if Bell(1, n):
        print('winnable')
    else:
        print('hopeless')