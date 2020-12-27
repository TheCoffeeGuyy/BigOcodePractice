n = int(input())
a = list(map(int, input().split()))

j = 0
diff = 0
cnt = [0] * 100005
maxRange = 0

for i in range(n):
  if (cnt[a[i]] == 0):
    diff += 1
  cnt[a[i]] += 1
  while  diff > 2:
    if cnt[a[j]] == 1:
      diff -= 1
    cnt[a[j]] -= 1
    j += 1
  maxRange = max(maxRange, i - j + 1)

print(maxRange)
