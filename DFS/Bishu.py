MAX = 1005
n = int(input())
results = []
import queue
graph = [[] for _ in range(MAX)]
for i in range(n -1 ):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

girlLocation = [None] * MAX
visited = [False] * MAX

girls = int(input())

for i in range(girls):
    girl = int(input())
    girlLocation[girl] = 1

q = queue.Queue()
q.put(1)
visited[1] = True
exit = False
while not q.empty():
    u = q.get()
    for v in graph[u]:
        if not visited[v]:
            visited[v] = True
            if girlLocation[v]:
                results.append(v)
                exit = True
            q.put(v)
    if exit:
        break

print(min(results))