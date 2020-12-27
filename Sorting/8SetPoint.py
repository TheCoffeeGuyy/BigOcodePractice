eightPoints = []
xValues = [False] * 1000005
yValues = [False] * 1000005
uniqueXs = []
uniqueYs = []

for _ in range(8):
  x, y = map(int, input().split())
  eightPoints.append([x,y])

  if xValues[x] == False:
    xValues[x] = True
    uniqueXs.append(x)

  if yValues[y] == False:
    yValues[y] = True
    uniqueYs.append(y)
if len(uniqueYs) != 3 or len(uniqueXs) != 3:
  print('ugly')
  exit()

eightPoints.sort()
uniqueXs.sort()
uniqueYs.sort()
index = 0
for i in range(3):
  for j in range(3):
    if i == j == 1:
      continue
    if uniqueXs[i] == eightPoints[index][0] and uniqueYs[j] == eightPoints[index][1]:
      index += 1
    else:
      print('ugly')
      exit()


print('respectable')