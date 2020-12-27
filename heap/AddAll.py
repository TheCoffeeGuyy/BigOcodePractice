import queue
q = queue.PriorityQueue()

while True:
    n = int(input())
    if n == 0:
        break
    a = list(map(int, input().split()))
    for i in range(n):
        q.put(a[i])
    sum = 0
    while q.qsize() > 1:
        a1 = q.get()
        a2 = q.get()
        sum += a1 + a2
        q.put(a1 + a2)
    
    print(sum)
    q.get()