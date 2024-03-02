import sys






# import sys


# r, c = map(int, sys.stdin.readline().split())
# board = [list(map(int, sys.stdin.readline().split())) for _ in range(r)]

# cnt_prev = 0
# for i in range(r):
#     for j in range(c):
#         if board[i][j] == 1:
#             cnt_prev += 1

# time = 0
# while True:
#     cnt = 0
#     melt = [[False for _ in range(c)] for _ in range(r)]
#     for x in range(r):
#         for y in range(c):
#             if board[x][y] == 1:
#                 cnt += 1
#             for nx, ny in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
#                 if nx < 0 or nx > r - 1 or ny < 0 or ny > c - 1:
#                     continue
#                 if board[nx][ny] == 0:
#                     melt[x][y] = True
#                     break

#     for x in range(r):
#         for y in range(c):
#             if melt[x][y]:
#                 board[x][y] = 0

#     for i in range(r):
#         print(board[i])
#     print("===================")
    
#     if cnt == 0:
#         print("녹기 한 시간 전 치즈칸 ", cnt_prev)
#         break

#     cnt_prev = cnt
#     time += 1


# print(time)