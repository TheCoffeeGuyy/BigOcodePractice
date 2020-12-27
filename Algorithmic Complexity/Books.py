n, t = map(int, input().split())
a = list(map(int, input().split()))
maxBooks = readBooks = 0
j = 0
for i in range(n):
  while t < a[i]:
    t += a[j]
    j += 1
    readBooks -= 1;
  t -= a[i]
  readBooks += 1
  maxBooks = max(maxBooks, readBooks)

print(maxBooks)
