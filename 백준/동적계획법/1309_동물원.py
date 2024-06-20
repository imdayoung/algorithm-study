import sys

N = int(sys.stdin.readline())
dp = [1] * (N + 1)
dp[1] = 3
for i in range(2, N + 1):
    dp[i] = dp[i - 1] * 2 + dp[i - 2]

print(dp[N] % 9901)