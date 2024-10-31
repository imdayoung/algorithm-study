def solution(m, n, puddles):
    graph = [[1 for _ in range(m)] for _ in range(n)]
    
    if puddles != [[]]:
        for i, j in puddles:
            graph[j - 1][i - 1] = 0
        
    dp = [[1 for _ in range(m)] for _ in range(n)]
    
    for i in range(n):
        for j in range(m):
            if i == 0 and j == 0:
                continue
            if i == 0:
                if graph[i][j - 1] == 0 or graph[i][j] == 0:
                    dp[i][j] = 0
                else:
                    dp[i][j] = dp[i][j - 1]
            elif j == 0:
                if graph[i - 1][j] == 0 or graph[i][j] == 0:
                    dp[i][j] = 0
                else:
                    dp[i][j] = dp[i - 1][j]
            elif graph[i][j] == 0:
                dp[i][j] = 0
            else:
                dp[i][j] = (dp[i - 1][j] + dp[i][j - 1]) % 1000000007
                
    return dp[n - 1][m - 1]