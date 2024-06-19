import sys


N, K = map(int, sys.stdin.readline().split())
nums = [0] + list(map(int, sys.stdin.readline().split()))

dp = [[0 for _ in range(K + 1)] for _ in range(N + 1)]
for i in range(1, N + 1):
    for j in range(K + 1):
        if nums[i] % 2 == 0:
            dp[i][j] = dp[i - 1][j] + 1
        if j != 0 and nums[i] % 2 == 1:
            dp[i][j] = dp[i - 1][j - 1]

# for i in range()