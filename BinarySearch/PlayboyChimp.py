def binarySearchLower(a, left, right, x):
    result = -1    
    while left <= right:
        mid = (left + right) // 2
        if a[mid] < x:
            result = mid
            left = mid + 1
        else:
            right = mid - 1
    if result == -1: 
        return 'X'
    else:
        return a[result]

def binarySearchUpper(a, left, right, x):
    result = right
    while left <= right:
        mid = (left + right) // 2
        if a[mid] > x:
            result = mid
            right = mid - 1
        else:
            left = mid + 1
    if result == right: 
        return 'X'
    else:
        return a[result]
# a = [3,4,5,7, 9, 10, 12, 14, 15]
# print(binarySearchLower(a, 0, len(a) - 1, 10))
# print(binarySearchUpper(a, 0, len(a) - 1, 10))
    
n = int(input())
a = list(map(int, input().split()))

queryNumber = int(input())
queries = list(map(int, input().split()))

for x in queries:
    up = binarySearchUpper(a, 0, n - 1, x)
    down = binarySearchLower(a, 0, n - 1, x)
    print(down, up)