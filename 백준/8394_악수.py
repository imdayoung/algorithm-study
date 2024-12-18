import sys


n = int(sys.stdin.readline())

dp = [1 for _ in range(n + 1)]
for i in range(2, n + 1):
    dp[i] = (dp[i - 1] + dp[i - 2]) % 10

print(dp[n])
