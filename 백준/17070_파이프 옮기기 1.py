# 3차원 dp: 가로 0, 세로1, 대각선2
import sys


VER = 0
HOR = 1
DIA = 2
N = int(sys.stdin.readline())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

dp = [[[0 for _ in range(3)] for _ in range(N)] for _ in range(N)]

for j in range(1, N):
    if graph[0][j] == 1:
        break
    dp[0][j][VER] = 1

for i in range(1, N):
    for j in range(1, N):
        if graph[i][j] == 1:
            continue

        dp[i][j][VER] = dp[i][j - 1][VER] + dp[i][j - 1][DIA]
        dp[i][j][HOR] = dp[i - 1][j][HOR] + dp[i - 1][j][DIA]
        if graph[i - 1][j] == 0 and graph[i][j - 1] == 0:
            dp[i][j][DIA] = dp[i - 1][j - 1][VER] + dp[i - 1][j - 1][HOR] + dp[i - 1][j - 1][DIA]

print(dp[-1][-1][VER] + dp[-1][-1][HOR] + dp[-1][-1][DIA])