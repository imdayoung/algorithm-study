import sys


answer = []

max_value = 30
dp = [[0 for _ in range(max_value + 1)] for _ in range(max_value + 1)]

for j in range(max_value + 1):
    dp[0][j] = 1

for i in range(1, max_value + 1):
    for j in range(1, max_value + 1):
        if i > j:
            continue
        dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

while True:
    N = int(sys.stdin.readline())
    if N == 0:
        break
    answer.append(dp[N][N])

print(*answer, sep = "\n")