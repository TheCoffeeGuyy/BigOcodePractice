import queue
pq = queue.PriorityQueue()
removePQ = queue.PriorityQueue()
n = int(input())
for i in range(n):
    req = input().split()
    if req[0] == '1':
        pq.put(int(req[1]))
    elif req[0] == '2':
        removePQ.put(int(req[1]))
    else:
        while not removePQ.empty() and removePQ.queue[0] == pq.queue[0]:
            pq.get()
            removePQ.get()
        print(pq.queue[0])
