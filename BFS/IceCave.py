import queue
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
MAX = 501
table = [None] * MAX

def BFS(sr, sc, dr, dc):
  q = queue.Queue()
  table[sr][sc] = 'X'
  q.put((sr, sc))
  while q.qsize() > 0:
    ur, uc = q.get()
    for i in range(4):
      r = ur + dx[i]
      c = uc + dy[i]
      
      if r == dr and c == dc and table[r][c] == 'X':
        return True
      if r in range(n) and c in range(m) and table[r][c] == '.':
        table[r][c] = 'X'
        q.put((r, c))

  return False

n, m = map(int, input().split())
for i in range(n):
  table[i] = list(input())
# print(table)
sr, sc = map(int, input().split())
desR, desC = map(int, input().split())
if BFS(sr - 1, sc - 1, desR - 1, desC - 1):
  print('YES')
else:
  print('NO')
