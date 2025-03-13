N, P, Q, X, Y = map(int, input().split())

if N == 0:
    print(1)
    exit()
    
dp = [0 for _ in range(N + 1)]
dp[0] = 1


