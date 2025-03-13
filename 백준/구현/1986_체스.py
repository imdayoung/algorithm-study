import sys


answer = 0

n, m = map(int, sys.stdin.readline().split())
board = [[0 for _ in range(m)] for _ in range(n)]

queens = list(map(int, sys.stdin.readline().split()))
for i in range(1, len(queens), 2):
    board[queens[i] - 1][queens[i + 1] - 1] = 1

knights = list(map(int, sys.stdin.readline().split()))
for i in range(1, len(knights), 2):
    board[knights[i] - 1][knights[i + 1] - 1] = 2

pawns = list(map(int, sys.stdin.readline().split()))
for i in range(1, len(pawns), 2):
    board[pawns[i] - 1][pawns[i + 1] - 1] = 3

dx_q = [0, 1, 0, -1, 1, 1, -1, -1]
dy_q = [1, 0, -1, 0, 1, -1, 1, -1]
dx_k = [1, 1, -1, -1, 2, 2, -2, -2]
dy_k = [-2, 2, -2, 2, -1, 1, -1, 1]

for i in range(1, len(queens), 2):
    x = queens[i] - 1
    y = queens[i + 1] - 1
    for i in range(8):
        nx = x + dx_q[i]
        ny = y + dy_q[i]
        
        while 0 <= nx <= n - 1 and 0 <= ny <= m - 1 and board[nx][ny] < 1:
            board[nx][ny] = -1
            nx += dx_q[i]
            ny += dy_q[i]
    
for i in range(1, len(knights), 2):
    x = knights[i] - 1
    y = knights[i + 1] - 1
    for i in range(8):
        nx = x + dx_k[i]
        ny = y + dy_k[i]
        if nx < 0 or nx > n - 1 or ny < 0 or ny > m - 1 or board[nx][ny] != 0:
            continue
        board[nx][ny] = -1

for i in range(n):
    for j in range(m):
        if board[i][j] == 0:
            answer += 1

print(answer)
