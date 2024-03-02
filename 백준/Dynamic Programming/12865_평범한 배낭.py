import sys
input = sys.stdin.readline

# 물품의 수 n, 버틸 수 있는 무게 k
n, k = map(int, input().split())
dp = [[0] * (k + 1) for _ in range(n + 1)]
objs = [[0, 0]]

for _ in range(n):
    objs.append(list(map(int, input().split())))

for i in range(1, n + 1):
    for j in range(1, k + 1):
        weight = objs[i][0]
        value = objs[i][1]

        if weight > j:
            dp[i][j] = dp[i - 1][j]
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - weight] + value)

print(dp[n][k])