import queue
n, m = map(int, input().split())
catPosition =  list(map(int, input().split()))
catPosition.insert(0, 0)
MAX = 100005
graph = [[] for _ in range(MAX)]
for i in range(1, n):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)


visited = [False] * MAX
cats = [0] * MAX
def BFS(s):
  countRestaurants = 0
  visited[s] = True
  q = queue.Queue()
  q.put(s)
  if catPosition[s] == 1:
    cats[s] = 1
  while not q.empty():
    u = q.get()
    for v in graph[u]:
      if not visited[v]:
        visited[v] = True
        if catPosition[v] == 1:
          cats[v] = cats[u] + 1
        if cats[v] <= m:
          if len(graph[v]) == 1:
            countRestaurants += 1
          else: q.put(v)
  return countRestaurants
print(BFS(1))

a = [[]] * 5
a[1].append(1)
print(a)