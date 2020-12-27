n = int(input())
a = list(map(int, input().split()))

kills = 0
j = n - 1

for i in range(n - 1, -1, -1):
  j = min(i, j)
  lastPosition = max(0, i - a[i])
  if j > lastPosition:
    kills += (j - lastPosition)
    j = max(0, i - a[i])
print(n - kills)