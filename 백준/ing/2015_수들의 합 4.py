import sys


answer = 0

N, K = map(int, sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().split()))


# 시간 초과 ..
# import sys


# answer = 0

# N, K = map(int, sys.stdin.readline().split())
# nums = list(map(int, sys.stdin.readline().split()))

# sums = [0 for _ in range(N)]
# for i in range(N):
#     sums[i] = sums[i - 1] + nums[i]

# for i in range(N):
#     for j in range(i):
#         if sums[i] - sums[j] == K:
#             answer += 1
    
# print(answer)
