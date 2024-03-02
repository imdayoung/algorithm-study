import sys
input = sys.stdin.readline

def bfs(board):
    temp = [["O" for _ in range(C)] for _ in range(R)]
    for x in range(R):
        for y in range(C):
            if board[x][y] == "O":
                temp[x][y] = "."
                for k in range(4):
                    nx = x + dx[k]
                    ny = y + dy[k]
                    if nx < 0 or nx > R - 1 or ny < 0 or ny > C - 1:
                        continue
                    temp[nx][ny] = "."

    return temp


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

R, C, N = map(int, input().split())
# 초기 상태
board_initial = [list(map(str, input().rstrip())) for _ in range(R)]
# 모두 폭탄이 설치된 상태
board_all_bomb = [["O" for _ in range(C)] for _ in range(R)]
# 첫 번째 폭탄이 터진 상태
board_bomb_first = bfs(board_initial)
# 두 번째 폭탄이 터진 상태
board_bomb_second = bfs(board_bomb_first)

if N == 1:
    for i in range(R):
        print(''.join(board_initial[i]))
elif N % 2 == 0:
    for i in range(R):
        print(''.join(board_all_bomb[i]))
elif N % 4 == 3:
    for i in range(R):
        print(''.join(board_bomb_first[i]))
elif N % 4 == 1:
    for i in range(R):
        print(''.join(board_bomb_second[i]))