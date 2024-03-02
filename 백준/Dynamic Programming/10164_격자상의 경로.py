import sys


N, M, K = map(int, sys.stdin.readline().split())
dp = [[0 for _ in range(M)] for _ in range(N)]

# 첫 행과 첫 열은 갈 수 있는 길이 한 개 초기화
for i in range(N):
    dp[i][0] = 1
for i in range(M):
    dp[0][i] = 1

# O 표시가 되어 있는 칸이 없는 경우
if K == 0:
    for i in range(1, N):
        for j in range(1, M):
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

    print(dp[N - 1][M - 1])
# O 표시가 되어 있는 칸이 있는 경우
else:
    # O 표시가 되어 있는 칸의 좌표 찾기
    target_x, target_y = 0, 0
    num = 1
    for i in range(N):
        for j in range(M):
            if num == K:
                target_x, target_y = i, j
                break
            num += 1
        if target_x != 0 or target_y != 0:
            break

    # O 표시가 되어 있는 칸까지 갈 수 있는 방법의 수 찾기
    for i in range(1, target_x + 1):
        for j in range(1, target_y + 1):
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
    temp = dp[target_x][target_y]

    dp[target_x][target_y] = 1

    # 첫 행과 첫 열은 갈 수 있는 길이 한 개 초기화
    for i in range(target_x, N):
        dp[i][target_y] = 1
    for i in range(target_y, M):
        dp[target_x][i] = 1

    # O 표시가 되어 있는 칸에서 목표 칸까지 갈 수 있는 방법의 수 찾기
    for i in range(target_x + 1, N):
        for j in range(target_y + 1, M):
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

    print(temp * dp[N - 1][M - 1])