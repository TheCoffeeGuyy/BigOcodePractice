import queue
Max = 100
V = None
E = None
visited = [False for i in range(Max)]
path = [0 for i in range(Max)]
graph = [[] for i in range(Max)]

def BFS(s):
    for i in range(V):
        visited[i] = False
        path[i] = -1
    q = queue.Queue()
    visited[s] = True
    q.put(s)
    while not q.empty():
        u = q.get()
        for v in graph[u]:
            if not visited[v]:
                visited[v] = True
                q.put(v)
                path[v] = u

def findPath(start, end):
    if start == end:
        print(end, end=' ')
    elif path[end] == -1:
        print('No path')
    else:
        findPath(start, path[end])
        print(end, end=' ')

if __name__ == '__main__':
    V, E = map(int, input().split())
    for i in range(E):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
    print(graph)
    s = 0
    f = 5
    BFS(s)
    print(path)
    findPath(s, f)