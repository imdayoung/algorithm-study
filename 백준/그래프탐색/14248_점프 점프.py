def dfs(cnt, cur):
    if cur < 1 or cur > n or visitable[cur] or cnt == 2  ** n:
        return
    
    visitable[cur] = True
    
    dfs(cnt + 1, cur + A[cur])
    dfs(cnt + 1, cur - A[cur])


answer = 0

n = int(input())
A = [0]  + list(map(int, input().split()))
s = int(input())
visitable = [False for _ in range(n + 1)]

rocks = [i for i in range(1, n + 1)]
dfs(0, s)
for v in visitable:
    if v:
        answer += 1

print(answer)
