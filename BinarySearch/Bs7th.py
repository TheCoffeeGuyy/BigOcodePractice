n, k = map(int, input().split())
a = list(map(int, input().split()))
a.sort()

def binarySearch(a, left, right, x):
    while left <= right:
        mid = (left + right) // 2
        if a[mid] == x:
            return True
        elif a[mid] > x:
            right = mid - 1
        else: left = mid + 1
    return False
count = 0
for i in range(n):
    if binarySearch(a, i + 1, n - 1, abs(k + a[i])):
        count += 1
print(count)

