import queue
class Car:
  def __init__(self, id, arriveTime):
    self.id = id
    self.arriveTime = arriveTime


Q = int(input())

for x in range(Q):
  n, t, m = map(int, input().split())
  curTime = 0
  curSide = 0
  qSide = [[], []]
  qSide[0] = queue.Queue()
  qSide[1] = queue.Queue()
  result = [0] * 10005

  for i in range(m):
    arriveTime, side = input().split()
    if side == 'left':
      qSide[0].put(Car(i, int(arriveTime)))
    else:
      qSide[1].put(Car(i, int(arriveTime)))

  waiting = (not qSide[0].empty()) + (not qSide[1].empty())
  while waiting:
    if waiting == 1:
      if qSide[0].empty():
        nextTime = qSide[1].queue[0].arriveTime
      else:
        nextTime = qSide[0].queue[0].arriveTime
    else:
      nextTime = min(qSide[0].queue[0].arriveTime, qSide[1].queue[0].arriveTime)
    curTime = max(nextTime, curTime)
    cars = 0
    while not qSide[curSide].empty():
      car = qSide[curSide].queue[0]
      if car.arriveTime <= curTime and cars < n:
        result[car.id] = curTime + t
        cars += 1
        qSide[curSide].get()
      else:
        break

    curTime += t
    curSide = 1 - curSide
    waiting = (not qSide[0].empty()) + (not qSide[1].empty())
  for i in range(m):
    print(result[i])
  if x != Q - 1:
    print()
