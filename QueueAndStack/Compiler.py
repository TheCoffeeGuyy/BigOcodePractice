n = int(input())
for _ in range(n):
  p = input()
  ans = 0
  stack = []
  for i in range(len(p)):
    if p[i] == '<':
      stack.append(p[i])
    elif len(stack) == 0:
      break
    else:
      stack.pop()
      if len(stack) == 0:
        ans = i + 1
  print(ans)