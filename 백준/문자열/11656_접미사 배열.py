s = input()
ans = []

for i in range(len(s)):
    ans.append(s[i:len(s) + 1])

ans.sort()
for i in ans:
    print(i)