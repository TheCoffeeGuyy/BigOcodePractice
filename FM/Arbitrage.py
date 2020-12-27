def FM(dist):
    for k in range(N):
        for i in range(N):
            for j in range(N):
                dist[i][j] = max(dist[i][j], dist[i][k] * dist[k][j])

test = 1
while True:
    N = int(input())
    if N == 0:
        break
    currencies = []
    dist = [[ 1 if i == j else 0 for j in range(N) ] for i in range(N)]
    for i in range(N):
        currency = input()
        currencies.append(currency)
    
    M = int(input())
    for i in range(M):
        cur, ratio, anotherCur = input().split()
        indexOfCur = currencies.index(cur)
        indexOfAnotherCur = currencies.index(anotherCur)
        dist[indexOfCur][indexOfAnotherCur] = float(ratio)
    
    FM(dist)
    result = 'No'
    for i in range(N):
        if dist[i][i] > 1:
            result = 'Yes'

    print('Case {}: {}'.format(test, result))
    input()
    test += 1