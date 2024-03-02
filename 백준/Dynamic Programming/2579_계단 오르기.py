import sys
input = sys.stdin.readline

n = int(input())
steps = [int(input()) for _ in range(n)]
dp = steps[:1] + [0 for _ in range(n)]

for i in range(1, n):
    dp[i] = max(dp[i - 3] + steps[i - 1] + steps[i], dp[i - 2] + steps[i])

print(dp[n - 1])