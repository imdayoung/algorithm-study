import sys


dp = [[0 for _ in range(10)] for _ in range(65)]
for j in range(10):
    dp[1][j] = 1

for i in range(2, 65):
    for j in range(10):
        for k in range(j, 10):
            dp[i][k] += dp[i - 1][j]

T = int(sys.stdin.readline())
for _ in range(T):
    n = int(sys.stdin.readline())
    print(sum(dp[n]))
