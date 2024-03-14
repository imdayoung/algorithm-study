import sys


max_value = 100000
dp = [1] * (max_value + 1)

for i in range(2, max_value + 1):
    dp[i] += dp[i - 2]

for i in range(3, max_value + 1):
    dp[i] += dp[i - 3]

T = int(sys.stdin.readline())
for _ in range(T):
    n = int(sys.stdin.readline())
    print(dp[n])


# # 시간초과 -> DP인가봐 ..
# import sys
# sys.setrecursionlimit(10 ** 6)


# def back_tracking(start, num, target):
#     global answer
#     if num == target:
#         answer += 1
#         return
#     if num > target:
#         return
    
#     for i in range(start, 3 + 1):
#         back_tracking(i, num + i, target)


# T = int(sys.stdin.readline())
# for _ in range(T):
#     answer = 0
#     n = int(sys.stdin.readline())
#     back_tracking(1, 0, n)
#     print(answer)