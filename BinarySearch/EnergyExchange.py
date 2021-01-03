n, k = map(int, input().split())
a = list(map(int, input().split()))
left = 0
right = 1000
while right - left > 1e-7:
    acc = 0
    mid = (left + right) / 2
    for i in range(n):
        
        acc += max(a[i] - mid, 0)
    if mid * n < sum(a) - acc * k / 100:
        left = mid
    else:
        right = mid

print('%.9f' %left)