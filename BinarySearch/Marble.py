case = 1

def firstSearch(a, left, right, x):
    if left <= right:
        mid = (left + right) // 2
        if a[mid] == x and (x > a[mid -1] or left == mid):
            return mid
        elif x > a[mid]:
            return firstSearch(a, mid + 1, right, x)
        else:
            return firstSearch(a, left, mid -1 ,x)
    return -1


while True:
    n, q = map(int, input().split())
    if n == 0 and q == 0:
        break
    a = []
    for i in range(n):
        numb = int(input())
        a.append(numb)
    a.sort()
    print('CASE# {}:'.format(case))
    for i in range(q):
        query = int(input())
        result = firstSearch(a, 0, len(a) - 1, query)
        if result == -1:
            print('{} not found'.format(query))
        else: print('{} found at {}'.format(query, result + 1))
    case +=1