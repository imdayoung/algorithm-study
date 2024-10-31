import sys
sys.stdin = open("input.txt", "r")

def dfs(start):
    global cnt
    if sum(temp) == K:
        cnt += 1
        return
    
    for i in range(start, N):
        temp.append(nums[i])
        dfs(i + 1)
        temp.pop()


T = int(input())
for tc in range(1, T + 1):
    cnt = 0
    temp = []

    N, K = map(int, input().split())
    nums = list(map(int, input().split()))
    dfs(0)
    print(f"#{tc} {cnt}")