from collections import deque
caseIndex = 1

while True:
  P, C = map(int, input().split())
  if P == 0 and C == 0:
    break
  print('Case {}:'.format(caseIndex))
  line = deque()
  for i in range(1, min(P,C) + 1, 1):
    line.append(i)
  for _ in range(C):
    query = input().split()
    char = query[0]
    if char == 'N':
      print(line[0])
      line.append(line.popleft())
    else:
      value = int(query[1])
      line.append(value)
      for j in range(len(line) - 1):
        if line[0] == value:
          line.popleft()
        else:
          line.append(line.popleft())
  caseIndex += 1
