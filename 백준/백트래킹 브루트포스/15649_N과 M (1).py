# 1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열

def dfs():
    if len(s) == M:
        print(' '.join(map(str, s)))
        return
    
    for i in range(1, N + 1):
        if i not in s:
            s.append(i)
            dfs()
            s.pop()

N, M = map(int, input().split())
s = []
dfs()