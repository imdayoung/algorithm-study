import sys
input = sys.stdin.readline


n = int(input())
grapes = [int(input()) for _ in range(n)]

dp = [0] * (n + 1)

if n == 1:
    print(grapes[0])

else:
    dp[1] = grapes[0]
    dp[2] = grapes[0] + grapes[1]
    for i in range(3, n + 1):
        dp[i] = max(dp[i - 1], dp[i - 2] + grapes[i - 1], dp[i - 3] + grapes[i - 2] + grapes[i - 1])

    print(dp[n])