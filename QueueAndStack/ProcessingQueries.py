import queue
n, b = map(int, input().split())
q = queue.Queue()
finishedTime = 0
for _ in range(n):
  t, d = map(int, input().split())

  while q.qsize() != 0 and t >= q.queue[0]:
    q.get()

  if q.qsize() <= b:
    finishedTime = max(t, finishedTime) + d
    q.put(finishedTime)
    print(finishedTime, end=' ')
  else:
    print(-1, end=' ')