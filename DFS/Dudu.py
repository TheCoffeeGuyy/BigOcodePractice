import sys
n = int(input())
documents, relations = map(int, input().split())
graph = [[] for _ in range(20)]
for i in range(relations):
    u,v = map(int, input().split())
    graph[u].append(v)
visited = [False] * 10005
sys.setrecursionlimit(10005)
def DFS(u):
    visited[u] = 1
 
    for v in graph[u]:
        if visited[v] == 1:
            return True
        elif visited[v] == 0:
            if DFS(v):
                return True
     
    visited[u] = 2
    return False
                
for _ in range(n):
    documents, relations = map(int, input().split())
    graph = [[] for _ in range(10005)]
    for i in range(relations):
        u,v = map(int, input().split())
        graph[u].append(v)
    visited = [0] * 10005
    for j in range(1, documents + 1):
        if not visited[j]:
            if DFS(j):
                print('YES')
            else: print('NO')
