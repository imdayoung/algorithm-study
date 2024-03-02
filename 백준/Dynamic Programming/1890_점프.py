import sys
input = sys.stdin.readline


N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
dp = [[0] * N for _ in range(N)]
dp[0][0] = 1

for i in range(N):
    for j in range(N):
        jump = board[i][j]
        if dp[i][j] > 0 and jump != 0:
            if i + jump < N:
                dp[i + jump][j] += dp[i][j]
            if j + board[i][j] < N:
                dp[i][j + jump] += dp[i][j]

print(dp[N - 1][N - 1])

# import sys
# input = sys.stdin.readline
# sys.setrecursionlimit(10 ** 6)


# def dfs(x, y):
#     global answer
#     if x > N - 1 or y > N - 1:
#         return
#     if board[x][y] == 0:
#         answer += 1
#         return
    
#     for nx, ny in [(x + board[x][y], y), (x, y + board[x][y])]:
#         dfs(nx, ny)


# answer = 0
# N = int(input())
# board = [list(map(int, input().split())) for _ in range(N)]
# for b in board:
#     print(b)
# dfs(0, 0)
# print(answer)