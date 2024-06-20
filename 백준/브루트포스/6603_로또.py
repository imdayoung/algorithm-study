import sys
input = sys.stdin.readline

def dfs(start):
    if len(s) == 6:
        print(' '.join(map(str, s)))
        return

    for i in range(start, k):
        if S[i] not in s:
            s.append(S[i])
            dfs(i + 1)
            s.pop()

nums = list(map(int, input().split()))
k = nums[0]
S = nums[1:]
while nums != [0]:
    S.sort()
    s = []
    dfs(0)
    print()
    nums = list(map(int, input().split()))
    k = nums[0]
    S = nums[1:]