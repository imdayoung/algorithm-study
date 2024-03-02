import sys
input = sys.stdin.readline

answer = 0

N, K = map(int, input().split())
nums = list(map(int, input().split()))
count = {i:0 for i in range(1, 100000 + 1)}

start, end = 0, 0
while end != N:
    if count[nums[end]] < K:
        count[nums[end]] += 1
        end += 1
    else:
        count[nums[start]] -= 1
        start += 1
    answer = max(answer, end - start)

print(answer)