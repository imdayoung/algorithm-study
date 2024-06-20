import sys
input = sys.stdin.readline


def back_tracking():
    if len(arr) == M:
        print(' '.join(map(str, arr)))
        return
    
    remember = 0
    for i in range(N):
        if not visited[i] and remember != nums[i]:
            visited[i] = True
            arr.append(nums[i])
            remember = nums[i]
            back_tracking()
            visited[i] = False
            arr.pop()

answer = []
N, M = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
arr = []
visited = [False] * N
back_tracking()
for a in answer:
    print(a)