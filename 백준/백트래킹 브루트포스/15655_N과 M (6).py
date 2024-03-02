# N개의 자연수 중에서 중복 없이 M개를 고른 수열
# 고른 수열은 오름차순

def dfs(start):
    if len(s) == M:
        print(' '.join(map(str, s)))
        return
    
    for i in range(start, N):
        if nums[i] not in s:
            s.append(nums[i])
            dfs(i + 1)
            s.pop()

N, M = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()

s = []
dfs(0)