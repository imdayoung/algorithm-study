import sys
input = sys.stdin.readline


n, k = map(int, input().split())
coins = sorted(list(set([int(input()) for _ in range(n)])))
dp = [-1] * (k + 1)
dp[0] = 0

for coin in coins:
    for price in range(coin, k + 1):
        # X원 동전의 배수인 경우
        if price % coin == 0:
            dp[price] = price // coin
        # 아직 경우의 수가 없는데 price-coin의 가치는 경우의 수가 있는 경우
        elif dp[price] == -1 and dp[price - coin] != -1:
            dp[price] = dp[price - coin] + 1
        # 경우의 수가 이미 있지만 더 작은 경우가 있을 수도 있는 경우
        elif dp[price] != -1 and dp[price - coin] != -1:
            dp[price] = min(dp[price], dp[price - coin] + 1)

answer = dp[k]
if answer == 0:
    print(-1)
else:
    print(answer)

    
# import sys
# input = sys.stdin.readline
# INF = int(1e9)

# n, k = map(int, input().split())
# coins = list(set([int(input()) for _ in range(n)]))
# dp = [INF] * (k + 1)

# for coin in coins:
#     if coin > k:
#         continue
#     dp[coin] = 1
    
# for price in range(coins[0], k + 1):
#     for i in range(price):
#         if dp[i] == INF or dp[price - i] == INF:
#             continue
#         dp[price] = min(dp[price], dp[price - i] + dp[i])

# answer = dp[k]
# if answer == INF:
#     print(-1)
# else:
#     print(answer)