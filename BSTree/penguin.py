n = int(input())
s = dict()
for i in range(n):
    penguin = input()
    if penguin in s:
        s[penguin] += 1
    else:
        s[penguin] = 1
max = 0
ans = ""
for x in s:
    if s[x] > max:
        max = s[x]
        ans =x
print(ans)