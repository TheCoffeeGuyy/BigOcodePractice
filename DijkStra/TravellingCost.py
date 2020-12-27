import queue
MAX = 505
INF = 10e9
n = int(input())
graph = [[] for i in range(500)]
dist = [INF for _ in range(MAX)]
class Node:
    def __init__(self, id, dist):
        self.id = id
        self.dist = dist
    def __lt__(self, otherNode):
        return self.dist <= otherNode.dist
    

for i in range(n):
    a, b, w = map(int, input().split())
    graph[a].append(Node(b, w))
    graph[b].append(Node(a, w))

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

s = int(input())
q = int(input())
Dijkstra(s)
for i in range(q):
    des = int(input())
    if (dist[des] != INF):
        print(dist[des])
    else:
        print('NO PATH')