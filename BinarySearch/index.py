a = [1,2,3,6,8,10,11,24,25,26,37]

def binarySearch(a, left, right, x):
    if left <= right:
        mid = (left + right) // 2
        if a[mid] == x:
            return mid
        if a[mid] > x:
            return binarySearch(a, left, mid -1 , x)
        return binarySearch(a, mid + 1, right , x)
# print(binarySearch(a, 0, len(a) - 1, 3))
