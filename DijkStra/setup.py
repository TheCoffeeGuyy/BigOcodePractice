import queue
max = 100
INF = int(10e9)

class Node:
    def __init__(self, id, dist):
        self.id = id
        self.dist = dist
    def __lt__(self, other):
        return self.dist <= other.dist

def Dijktra(s):
    pq = queue.PriorityQueue()
    pq.put(Node(s, 0))
    dist[0] = 0
    while not pq.empty():
        top = pq.get()
        u = top.id
        w = top.dist
        for neighbor in graph[u]:
            if w + neighbor.dist < dist[neighbor.id]:
                dist[neighbor.id] = w + neighbor.dist
                path[neighbor.id] = u
                pq.put(Node(neighbor.id, dist[neighbor.id]))

# def solve():
#     n = int(input())
#     graph = [[] for i in range(n +5)]
#     path = [INF for i in range(n + 5)]
