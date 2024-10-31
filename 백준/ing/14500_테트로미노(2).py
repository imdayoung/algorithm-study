import sys


def dfs(x, y, cnt, s):
    global answer
    if cnt == 4:
        answer = max(answer, s)
        return
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx > N - 1 or ny < 0 or ny > M - 1 or visited[nx][ny]:
            continue

        visited[nx][ny] = True
        dfs(nx, ny, cnt + 1, s + board[nx][ny])
        visited[nx][ny] = False


def check(x, y):
    global answer
    if x + 1 < N - 1 and y + 2 < M - 1:
        temp = board[x][y] + board[x][y + 1] + board[x][y + 2] + board[x + 1][y + 1]
        answer = max(answer, temp)

    if x + 2 < N - 1 and y + 1 < M - 1:
        temp = board[x][y] + board[x + 1][y] + board[x + 2][y] + board[x + 1][y + 1]
        answer = max(answer, temp)

    if x + 2 < N - 1 and y - 1 > 0:
        temp = board[x][y] + board[x + 1][y] + board[x + 2][y] + board[x + 1][y - 1]
        answer = max(answer, temp)
    
    if x + 1 < N - 1 and y - 1 > 0 and y + 1 < M - 1:
        temp = board[x][y] + board[x + 1][y - 1] + board[x + 1][y] + board[x + 1][y + 1]
        answer = max(answer, temp)


dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

answer = 0
N, M = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
visited = [[False for _ in range(M)] for _ in range(N)]

for i in range(N):
    for j in range(M):
        visited[i][j] = True
        dfs(i, j, 1, board[i][j])
        visited[i][j] = False
        check(i, j)

print(answer)
