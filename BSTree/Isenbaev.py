import queue
def BFS(graph, s, dist):
    q = queue.Queue()
    q.put(s)
    dist[s] = 0
    while q.qsize() != 0:
        u = q.get()
        for v in graph[u]:
            if dist[v] == 'undefined':
                dist[v] = dist[u] + 1
                q.put(v)

n = int(input())
S = dict()
cnt = 0
graph = []
for i in range(n):
    line = input().split()
    relations = []
    for name in line:
        if name in S:
            id = S[name]
        else:
            S[name] = cnt
            id = cnt
            cnt +=1
            graph.append([])
        relations.append(id)
    for u in relations:
        for v in relations:
            if u != v:
                graph[u].append(v)
        
dist = ['undefined' for i in range(cnt)]
if 'Isenbaev' in S:
    BFS(graph, S['Isenbaev'], dist)
a = []
for name in S:
    a.append(name)
a.sort()  
for name in a:
    print(name, dist[S[name]])