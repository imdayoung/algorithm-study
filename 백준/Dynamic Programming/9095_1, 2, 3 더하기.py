import sys
input = sys.stdin.readline

dp = [0, 1, 2, 4] + [0] * 8

for i in range(4, 12):
    dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]

T = int(input())
for _ in range(T):
    n = int(input())
    print(dp[n])