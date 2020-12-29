a = [1,2,2,2,2,2,2,2,3,6,8,10,11,24,25,26,37]

def binarySearch(a, left, right, x):
    if left <= right:
        mid = (left + right) // 2
        if a[mid] == x:
            return mid
        if a[mid] > x:
            return binarySearch(a, left, mid -1 , x)
        return binarySearch(a, mid + 1, right , x)
# print(binarySearch(a, 0, len(a) - 1, 3))

def firstIndexSearch(a, left, right, x):
    if left <= right:
        mid = (left + right) // 2
        if a[mid] == x and (x > a[mid - 1] or mid == left):
            return mid
        elif x > a[mid]:
            return firstIndexSearch(a, mid + 1, right, x)
        else:
            return firstIndexSearch(a, left, mid -1, x)
    return -1

def lastIndexSearch(a, left, right, x):
    if left <= right:
        mid = (left + right) // 2
        if a[mid] == x and (x < a[mid + 1] or mid == right):
            return mid
        elif x >= a[mid]:
            return lastIndexSearch(a, mid + 1, right, x)
        else:
            return lastIndexSearch(a, left, mid -1 , x)
    return -1

print(lastIndexSearch(a, 0, len(a) - 1, 2))