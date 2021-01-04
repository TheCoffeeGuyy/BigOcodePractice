t = int(input())

for i in range(t):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    friends = set()
    for j in range(n):
        friends.add(a[j])
    for k in range(n, n + m):
        if a[k] in friends:
            print('YES')
        else:
            print('NO')
        friends.add(a[k])