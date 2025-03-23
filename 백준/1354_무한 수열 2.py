def backtracking(num):
    if num <= 0:
        return 1
    
    value = dp.get(num)
    if value:
        return value
    
    px = backtracking(num // P - X)
    qy = backtracking(num // Q - Y)
    dp[num] = px + qy
    return dp[num]
    

N, P, Q, X, Y = map(int, input().split())

if N == 0:
    print(1)
    exit()
    
dp = {}
    
backtracking(N)
print(dp[N])
