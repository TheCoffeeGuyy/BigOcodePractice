t = int(input())

for _ in range(t):
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    s = set()
    for el in a:
        s.add(el)
    if s.__len__() == x:
        print('Good')
    elif s.__len__() > x:
        print('Average')
    else:
        print('Bad')