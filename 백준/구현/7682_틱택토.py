import sys


def bingo_cnt(board, temp):
    bingo = 0

    if board[0][0] == temp:
        if board[0][1] == temp and board[0][2] == temp:
            bingo += 1
        if board[1][0] == temp and board[2][0] == temp:
            bingo += 1
        if board[1][1] == temp and board[2][2] == temp:
            bingo += 1

    if board[1][0] == temp and board[1][1] == temp and board[1][2] == temp:
            bingo += 1

    if board[2][0] == temp:
        if board[2][1] == temp and board[2][2] == temp:
            bingo += 1
        if board[1][1] == temp and board[0][2] == temp:
            bingo += 1
        
    if board[0][1] == temp and board[1][1] == temp and board[2][1] == temp:
        bingo += 1

    if board[0][2] == temp and board[1][2] == temp and board[2][2] == temp:
        bingo += 1

    return bingo


def char_cnt(board):
    x, o = 0, 0

    for i in range(3):
        for j in range(3):
            if board[i][j] == 'X':
                x += 1
            elif board[i][j] == 'O':
                o += 1

    return x, o


answers = []
while True:
    temp = list(map(str, sys.stdin.readline().rstrip()))
    if temp == ['e', 'n', 'd']:
        break

    board = [[temp[i], temp[i + 1], temp[i + 2]] for i in range(0, 7, 3)]

    x_bingo = bingo_cnt(board, 'X')
    o_bingo = bingo_cnt(board, 'O')

    x, o = char_cnt(board)

    if x_bingo >= 1 and o_bingo == 0 and x - o == 1:
        answers.append('valid')
    elif o_bingo == 1 and x_bingo == 0 and x == o:
        answers.append('valid')
    elif x_bingo == 0 and o_bingo == 0 and x == 5 and o == 4:
        answers.append('valid')
    else:
        answers.append('invalid')

for answer in answers:
    print(answer)
    

# import sys


# def bingo_cnt(board, temp):
#     # 1 첫 번째 가로줄 2 첫 번째 세로줄 3 대각선\ 4 두번째 가로줄
#     # 5 세 번째 가로줄 6 대각선/ 7두번째 세로줄 8세번째 세로줄

#     bingo_status = []
#     bingo = 0

#     if board[0][0] == temp:
#         if board[0][1] == temp and board[0][2] == temp:
#             bingo += 1
#             bingo_status.append(1)
#         if board[1][0] == temp and board[2][0] == temp:
#             bingo += 1
#             bingo_status.append(2)
#         if board[1][1] == temp and board[2][2] == temp:
#             bingo += 1
#             bingo_status.append(3)

#     if board[1][0] == temp and board[1][1] == temp and board[1][2] == temp:
#             bingo += 1
#             bingo_status.append(4)

#     if board[2][0] == temp:
#         if board[2][1] == temp and board[2][2] == temp:
#             bingo += 1
#             bingo_status.append(5)
#         if board[1][1] == temp and board[0][2] == temp:
#             bingo += 1
#             bingo_status.append(6)
        
#     if board[0][1] == temp and board[1][1] == temp and board[2][1] == temp:
#         bingo += 1
#         bingo_status.append(7)

#     if board[0][2] == temp and board[1][2] == temp and board[2][2] == temp:
#         bingo += 1
#         bingo_status.append(8)

#     return bingo, bingo_status


# def char_cnt(board):
#     x, o, dot = 0, 0, 0

#     for i in range(3):
#         for j in range(3):
#             if board[i][j] == 'X':
#                 x += 1
#             elif board[i][j] == 'O':
#                 o += 1
#             else:
#                 dot += 1

#     return x, o, dot


# answers = []
# while True:
#     temp = list(map(str, sys.stdin.readline().rstrip()))
#     if temp == ['e', 'n', 'd']:
#         break

#     board = [[temp[i], temp[i + 1], temp[i + 2]] for i in range(0, 7, 3)]

#     x_bingo, x_bingo_status = bingo_cnt(board, 'X')
#     o_bingo, o_bingo_status = bingo_cnt(board, 'O')

#     x, o, dot = char_cnt(board)

#     if x_bingo == 0 and o_bingo == 0 and dot != 0:
#         # print(1)
#         answers.append('invalid')
#     elif o > x:
#         # print(2)
#         answers.append('invalid')
#     elif x_bingo > 0 and o_bingo > 0:
#         # print(3)
#         answers.append('invalid')
#     elif o_bingo > 1:
#         # print(4)
#         answers.append('invalid')
#     elif x_bingo == 1 and x == o:
#         answers.append('invalid')
#     elif o_bingo == 1 and dot == 0:
#         answers.append('invalid')
#     elif x_bingo > 1:
#         if x_bingo_status in [[1, 8], [1, 2], [2, 5], [5, 8], [2, 4], [5, 7], [4, 8], [1, 7], [1, 3], [2, 3], [3, 8], [3, 5], [1, 6], [2, 6], [5, 6], [6, 8]]:
#             # print(5)
#             answers.append('valid')
#         else:
#             # print(6)
#             answers.append('invalid')
#     elif abs(x - o) > 1:
#         # print(7)
#         answers.append('invalid')
#     else:
#         # print(8)
#         answers.append('valid')

# for answer in answers:
#     print(answer)