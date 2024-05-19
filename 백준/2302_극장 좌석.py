# 17M
import sys


answer = 1

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
vips = [int(sys.stdin.readline()) for _ in range(M)]

if N == 1:
    answer = 1
    
elif N == 2:
    if M == 1 or M == 2:
        answer = 1

    else:
        answer = 2
else:
    dp = [0 for _ in range(N + 1)]
    dp[1] = 1
    dp[2] = 2
    for i in range(3, N + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    temp = [0]
    end = N + 1

    for i in range(M + 1):
        print(dp[temp[i + 1] - temp[i] - 1])
        answer *= dp[temp[i + 1] - temp[i] - 1]

print(answer)