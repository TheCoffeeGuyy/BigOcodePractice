import queue
n = int(input())
a = list(map(int, input().split()))
pq = queue.PriorityQueue()
for i in range(n):
    pq.put(-a[i])
    if i < 2:
        print(-1)
    else:
        a1 = -pq.get()
        a2 = -pq.get()
        a3 = -pq.get()
        print(a1 * a2 * a3)
        pq.put(-a1)
        pq.put(-a2)
        pq.put(-a3)
