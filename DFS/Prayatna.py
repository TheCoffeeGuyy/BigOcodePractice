query = int(input())

def DFS(s):
    q = [s]
    visited[s] = True
    while len(q) > 0:
        u = q.pop()
        for v in graph[u]:
            if not visited[v]:
                visited[v] = True
                q.append(v)


for _ in range(query):
    node = int(input())
    relations = int(input())
    graph = [[] for _ in range(node)]
    for i in range(relations):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
    visited = [False] * node
    totalMetPeers = 0
    for i in range(node):
        if not visited[i]:
            # DFS go here
            DFS(i)
            totalMetPeers += 1
    print(totalMetPeers)