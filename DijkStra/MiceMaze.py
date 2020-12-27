import queue
MAX = 110
INF = int(10e9) + 7
graph = [[] for i in range(MAX)]
dist = [INF for _ in range(MAX)]
class Node:
    def __init__(self, id, dist):
        self.id = id
        self.dist = dist
    def __lt__(self, otherNode):
        return self.dist < otherNode.dist

def Dijkstra(s):
    pq = queue.PriorityQueue()
    pq.put(Node(s, 0))
    dist[s] = 0
    while not pq.empty():
        top = pq.get()
        id = top.id
        w = top.dist
        for neighbor in graph[id]:
            if w + neighbor.dist < dist[neighbor.id]:
                dist[neighbor.id] = w + neighbor.dist
                pq.put(Node(neighbor.id, dist[neighbor.id]))

N = int(input())
E = int(input())
T = int(input())
M = int(input())

for i in range(M):
    a, b, w = map(int, input().split())
    graph[b].append(Node(a, w))

Dijkstra(E)

count = 0
for i in range(1, N + 1):
    if dist[i] <= T:
        count += 1

print(count)