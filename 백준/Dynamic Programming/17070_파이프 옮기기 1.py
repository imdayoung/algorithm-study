import sys
HORIZONTAL, VERTICAL, DIAGNOAL = 0, 1, 2


N = int(sys.stdin.readline())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

dp = [[[0 for _ in range(N)] for _ in range(N)] for _ in range(3)]
dp[HORIZONTAL][0][1] = 1

for i in range(N):
    for j in range(2, N):
        # 가로, 세로 이동 가능
        if graph[i][j] == 0:
            dp[HORIZONTAL][i][j] = dp[HORIZONTAL][i][j - 1] + dp[DIAGNOAL][i][j - 1]
            dp[VERTICAL][i][j] = dp[VERTICAL][i - 1][j] + dp[DIAGNOAL][i - 1][j]

        # 대각선 이동 가능
        if graph[i][j] == 0 and graph[i - 1][j] == 0 and graph[i][j - 1] == 0:
            dp[DIAGNOAL][i][j] = dp[HORIZONTAL][i - 1][j - 1] + dp[VERTICAL][i - 1][j - 1] + dp[DIAGNOAL][i - 1][j - 1]

print(dp[HORIZONTAL][N - 1][N - 1] + dp[VERTICAL][N - 1][N - 1] + dp[DIAGNOAL][N - 1][N - 1])