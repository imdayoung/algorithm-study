import sys


def is_duplicated(x, y, n):
    # 행 검사
    for j in range(9):
        if sudoku[x][j] == n:
            return True
    # 열 검사
    for i in range(9):
        if sudoku[i][y] == n:
            return True
    # 네모 칸 검사
    for i in range(x // 3 * 3, x // 3 * 3 + 3):
        for j in range(y // 3 * 3, y // 3 * 3 + 3):
            if sudoku[i][j] == n:
                return True
    return False


def back_tracking(n):
    if n == len(blanks):
        for s in sudoku:
            print(*s)
        exit()
        
    x = blanks[n][0]
    y = blanks[n][1]
    for num in range(1, 10):
        if not is_duplicated(x, y, num):
            sudoku[x][y] = num
            back_tracking(n + 1)
            sudoku[x][y] = 0


sudoku = []
blanks = []
for i in range(9):
    temp = list(map(int, sys.stdin.readline().split()))
    sudoku.append(temp)
    for j in range(9):        
        if temp[j] == 0:
            blanks.append((i, j))

back_tracking(0)