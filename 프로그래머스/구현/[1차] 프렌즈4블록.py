def block_remove(m, n, board):
    # 블록을 지울 수 있는 지 판별
    can_remove = 0
    # 블록을 지운 후의 판
    new_board = [[0 for _ in range(m)] for _ in range(n)]
    # 지워지는 블록 표시
    will_removed = [[False for _ in range(n)] for _ in range(m)]

    # 지워지는 블록 구하기
    for i in range(m - 1):
        for j in range(n - 1):
            if board[i][j] != 0 and board[i][j] == board[i][j + 1] == board[i + 1][j] == board[i + 1][j + 1]:
                can_remove = 1
                will_removed[i][j] = True
                will_removed[i][j + 1] = True
                will_removed[i + 1][j] = True
                will_removed[i + 1][j + 1] = True

    # 지워지는 블록이 있는 경우
    if can_remove == 1:
        reversed_will_removed = [[a[i] for a in will_removed] for i in range(n)]
        for i in range(n):
            remained_block = []
            for j in range(m):
                if not reversed_will_removed[i][j]:
                    remained_block.append(board[j][i])
            temp = [0] * (m - len(remained_block))
            temp.extend(remained_block)
            new_board[i] = temp
        
        return can_remove, [[a[i] for a in new_board] for i in range(m)]
    
    # 지워지는 블록이 없는 경우
    else:
        return can_remove, board

    
def solution(m, n, board):
    answer = 0

    flag = 1
    while flag == 1:
        flag, board = block_remove(m, n, board)

    for i in range(m):
        for j in range(n):
            if board[i][j] == 0:
                answer += 1

    return answer