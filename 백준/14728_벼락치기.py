# 14M 46S
import sys


# 단원 개수 N, 공부할 수 있는 총 시간 T
N, T = map(int, sys.stdin.readline().split())
# 각 단원 별 예상 공부 시간 K, 그 단원 문제의 배점 S
subjects = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

dp = [[0 for _ in range(T)] for _ in range(N)]
for i in range(N):
    for j in range(T):
        time = subjects[i][0]
        point = subjects[i][1]

        if j < time:
            dp[i][j] = dp[i - 1][j]
        else:
            dp[i][j] = max(dp[i - 1][j - time] + point, dp[i - 1][j])

print(dp[-1][-1])