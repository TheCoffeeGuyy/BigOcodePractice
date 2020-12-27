INF = 10e9
N = 20

def FM(dist):
    for k in range(1,N + 1):
        for i in range(1,N + 1):
            for j in range(1,N + 1):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
test = 1
while True:
    # try: 
    dist = [[0 if i == j else INF for j in range(25)] for i in range(25)]
    for i in range(1, N ):
        # for j in list(map(int, input().split()))[1:]:
        #         dist[i][j] = dist[j][i] = 1
        line = list(map(int, input().split()))
        if (line[0] != 0):
            for j in range((line[0])):
                f = (line[j + 1])
                dist[i][f] = dist[f][i] = 1

    FM(dist)
    print('Test Set #{}'.format(test))
    q = int(input())
    for _ in range(q):
        u, v = map(int, input().split())
        print('{:2d} to {:2d}: {}'.format(u, v, dist[u][v]))
    test += 1
    print()
    # except EOFError:
    #     break
