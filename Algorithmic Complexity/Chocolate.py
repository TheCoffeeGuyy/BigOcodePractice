n = int(input())
t = list(map(int, input().split()))
aTotal = 0
bTotal = 0
i = 0
j = n - 1

while  i <= j:
  if aTotal + t[i] > bTotal + t[j]:
    bTotal += t[j]
    j -= 1
  else:
    aTotal += t[i]
    i += 1

print(i , n - i )

