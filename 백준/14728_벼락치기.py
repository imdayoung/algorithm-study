import sys


# 단원 개수 N, 공부할 수 있는 총 시간 T
N, T = map(int, sys.stdin.readline().split())
# 각 단원 별 예상 공부 시간 K, 그 단원 문제의 배점 S
subjects = [[0, 0]] + [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

dp = [[0 for _ in range(T + 1)] for _ in range(N + 1)]
for i in range(1, N + 1):
    time = subjects[i][0]
    point = subjects[i][1]

    for j in range(1, T + 1):
        if j < time:
            dp[i][j] = dp[i - 1][j]
        else:
            dp[i][j] = max(dp[i - 1][j - time] + point, dp[i - 1][j])

print(dp[N][T])