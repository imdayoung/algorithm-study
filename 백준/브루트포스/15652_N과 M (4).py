# 1부터 N까지 자연수 중에서 중복 허용하여 M개를 고른 수열
# 고른 수열은 오름차순

def dfs(start):
    if len(s) == M:
        print(' '.join(map(str, s)))
        return
    
    for i in range(start, N + 1):
        s.append(i)
        dfs(i)
        s.pop()

N, M = map(int, input().split())
s = []
dfs(1)