dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
MAX = 251;
slick = [0] * (MAX * MAX)
table = [None] * MAX
q = [None] * (MAX * MAX)

def BFS(sr, sc):
  left = 0
  right = 0
  table[sr][sc] = '0'
  q[0] = (sr, sc)
  count = 1

  while left <= right:
    ur, uc = q[left]
    left += 1
    for i in range(4):
      r = ur + dx[i]
      c = uc + dy[i]
      if r in range(N) and c in range(M) and table[r][c] == '1':
        table[r][c] = '0'
        right += 1
        q[right] = (r, c)
        count += 1

  slick[count] += 1

while True:
  N, M = map(int, input().split())
  if N == 0 and M == 0:
    break

  for i in range(N):
    table[i] = input().split()
    for j in range(M):
      slick[i * M + j +1] = 0

  slickCount = 0
  for i in range(N):
    for j in range(M):
      if (table[i][j] == '1'):
        BFS(i, j)
        slickCount += 1

  print(slickCount)

  for i in range(1, N * M +1):
    if slick[i] != 0:
      print(i, slick[i], sep=' ')

