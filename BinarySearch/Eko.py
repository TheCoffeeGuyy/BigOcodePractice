def calSum(a, mid):
    sum = 0
    for log in a:
        sum += max(log - mid, 0)
    return sum

def binarySearch(a, left, right, x):
    result = 0
    while left <= right:
        mid = (left + right) // 2
        if calSum(a, mid) >= x:
            result = mid
            left = mid + 1
        else:
            right = mid - 1
    return int(result)

n, m = map(int, input().split())

a = list(map(int, input().split()))

print(binarySearch(a, 0, 1e9, m))