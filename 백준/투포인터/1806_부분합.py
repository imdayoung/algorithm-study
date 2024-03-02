import sys


N, S = map(int, sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().split()))

answer = N + 1
start, end = 0, 0
total = 0

while True:
    # 합이 S보다 크거나 같은 경우
    if total >= S:
        answer = min(answer, end - start)
        total -= nums[start]
        start += 1

    # 합이 S보다 작은 경우
    elif total < S:
        if end == N:
            break
        total += nums[end]
        end += 1
        
if answer == N + 1:
    print(0)
else:
    print(answer)