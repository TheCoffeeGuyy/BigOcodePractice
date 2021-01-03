cases = int(input())
for case in range(1, cases + 1):
    lena = int(input())
    a = [0] + list(map(int, input().split()))
    res = 0
    left = 1
    right = a[-1] + 5
    while left <= right:
        mid = (left + right) // 2
        willIncrease = False
        k = mid
        for i in range(len(a) - 1):
            if a[i + 1] - a[i] > k:
                # increase estimated number
                willIncrease = True
                break
            elif a[i + 1] - a[i] == k:
                k -= 1

        if willIncrease:
            left = mid + 1
        else:
            res = mid
            right = mid - 1
    print('Case {}: {}'.format(case, res))