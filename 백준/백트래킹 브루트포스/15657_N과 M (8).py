import sys
input = sys.stdin.readline

def back_tracking(start):
    global answer
    if len(arr) == M:
        print(*arr)
        return
    
    for i in range(start, N):
        arr.append(nums[i])
        back_tracking(i)
        arr.pop()


N, M = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
arr = []
back_tracking(0)