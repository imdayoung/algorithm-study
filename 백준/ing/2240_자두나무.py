import sys


T, W = map(int, sys.stdin.readline().split())
jadus = [0]
for _ in range(T):
    jadus.append(int(sys.stdin.readline()))

dp = [[0 for _ in range(W + 1)] for _ in range(T + 1)]

for i in range(T + 1):
    if jadus[i] == 1:
        dp[i][0] = dp[i - 1][0] + 1
    else:
        dp[i][0] = dp[i - 1][0]

    for j in range(1, W + 1):
        if (jadus[i] == 1 and j % 2 == 0) or (jadus[i] == 2 and j % 2 != 0):
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - 1]) + 1
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - 1])

print(max(dp[T]))