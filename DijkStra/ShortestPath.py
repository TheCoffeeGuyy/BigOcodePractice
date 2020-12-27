from heapq import heappop, heappush
def DijkStra(s, f):
    dist = [10 ** 9] * (N + 1)
    pq = [(0, s)]
    dist[s] = 0

    while pq:
        width, id = heappop(pq)
        if id == f:
            break
        for w, city in graph[id]:
            if width + w < dist[city]:
                dist[city] = width + w
                heappush(pq, (dist[city], city))

    return dist[f]

cases = int(input())

for i in range(cases):
    N = int(input())
    cities = []
    graph = [[] for i in range(N + 1)]
    for j in range(1, N + 1):
        name = input()
        cities.append(name)
        relation = int(input())
        for a in range(relation):
            u, v = map(int, input().split())
            graph[j].append((v, u))

    numberAnswer = int(input())

    for b in range(numberAnswer):
        s, f = input().split()
        indexS = cities.index(s) + 1
        indexF = cities.index(f) + 1 
        print(DijkStra(indexS, indexF))
    print()