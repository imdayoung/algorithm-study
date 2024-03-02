import sys
    

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
vips = [int(sys.stdin.readline()) for _ in range(M)]
result = 1

if N > 1:
    dp = [1] * (N + 1)
    dp[1] = 1
    dp[2] = 2
    for i in range(3, N + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    if M == 0:
        result = dp[N]
    else:
        result *= dp[vips[0] - 1]
        for i in range(M - 1):
            result *= dp[vips[i + 1] - vips[i] - 1]
        result *= dp[N - vips[M - 1]]

print(result)