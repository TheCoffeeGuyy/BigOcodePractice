n = int(input())
listN = list(map(int, input().split()))
player = 0
results = [0, 0]
i = 0
j = n - 1

while i <= j:
  if listN[i] > listN[j]:
    results[player] += listN[i]
    i += 1
  else:
    results[player] += listN[j]
    j -= 1
  player = 1 - player

print(results[0], results[1])