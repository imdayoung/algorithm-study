N, K = map(int, input().split())
dp = [[0 for _ in range(K + 1)] for _ in range(N + 1)]

if K == 1:
    print(1)
    exit()
    
for i in range(1, N + 1):
    dp[i][1] = 1
    dp[i][2] = 1 + i

for j in range(3, K + 1):
    dp[1][j] = j

for i in range(2, N + 1):
    for j in range(3, K + 1):
        dp[i][j] = (dp[i - 1][j] + dp[i][j - 1]) % 1000000000
            
print(dp[N][K])