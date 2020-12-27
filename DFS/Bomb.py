n, m = map(int, input().split())
graph = [[] for _ in range(1000)]
for i in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)

exploded = [False] * 1000    
results = []
def DFS(s):
    q = [s]
    exploded[s] = True
    temp = 1
    while len(q) > 0:
        u = q.pop()
        for v in graph[u]:
            if not exploded[v]:
                q.append(v)
                exploded[v] = True
                temp += 1

    results.append(temp)

for i in range(1, 1 + n):
    exploded = [False] * 1000
    DFS(i)
print(max(results))