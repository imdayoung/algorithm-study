# N개의 자연수 중에서 중복 없이 M개를 고른 수열

def dfs():
    if len(s) == M:
        print(' '.join(map(str, s)))
        return
    
    for i in range(N):
        if nums[i] not in s:
            s.append(nums[i])
            dfs()
            s.pop()

N, M = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
s = []
dfs()