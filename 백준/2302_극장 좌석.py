import sys


answer = 1

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
vips = [0] + [int(sys.stdin.readline()) for _ in range(M)] + [N + 1]

if N == 1:
    answer = 1
else:
    dp = [1 for _ in range(N + 1)]
    dp[1] = 1
    for i in range(2, N + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    for i in range(M + 1):
        answer *= dp[vips[i + 1] - vips[i] - 1]

print(answer)
