a, b, x, y = map(int, input().split())
m = list(map(int, input().split()))
n = list(map(int, input().split()))
results = []
i = j = 0

while i < a and j < b:
  if n[j] <= m[i] + y and n[j] >= m[i] - x:
    results.append([i + 1, j + 1])
    i += 1
    j += 1
  elif n[j] < m[i] - x:
    j += 1
  elif n[j] > m[i] + y:
    i += 1

print(len(results))
for vest in results:
  print(vest[0], vest[1])