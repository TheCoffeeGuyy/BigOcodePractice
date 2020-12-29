def binarySearch(a, left, right, x):
    if left <= right:
        mid = (left + right) // 2
        if a[mid] == x:
            return mid
        if a[mid] > x:
            return binarySearch(a, left, mid -1 , x)
        return binarySearch(a, mid + 1, right , x)
    return -1


tests = int(input())
for _ in range(tests):
    n, m = map(int, input().split())
    listN = list(map(int, input().split()))
    listN.sort()
    count = 0
    for i in range(n):
        b = m - listN[i]
        if binarySearch(listN, i + 1, n - 1, b) != -1:
            count += 1
    print(count)