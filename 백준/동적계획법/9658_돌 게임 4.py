N = int(input())

dp = [-1 for _ in range(N + 5)]
dp[1] = "CY"
dp[2] = "SK"
dp[3] = "CY"
dp[4] = "SK"

for i in range(5, N + 1):
    if dp[i - 1] == "CY" or dp[i - 3] == "CY" or dp[i - 4] == "CY":
        dp[i] = "SK"
    else:
        dp[i] = "CY"

print(dp[N])
