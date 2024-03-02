import sys
input = sys.stdin.readline

def check_line(g, n):
    global win
    for i in range(1, 20):
        for j in range(1, 16):
            temp = g[i][j:j + 5]
            if temp == black_win:
                check = 1
                if [g[i][j - 1]] + temp != [check] * 6 and temp + [g[i][j + 5]] != [check] * 6:
                    win = check
                    if n == 1:
                        print(win)
                        print(i, j)
                    elif n == 2:
                        print(win)
                        print(j, i)
                    break
            elif temp == white_win:
                check = 2
                if [g[i][j - 1]] + temp != [check] * 6 and temp + [g[i][j + 5]] != [check] * 6:
                    win = check
                    if n == 1:
                        print(win)
                        print(i, j)
                    elif n == 2:
                        print(win)
                        print(j, i)
                    break
        if win != 0:
            break

def check_diag(g):
    global win
    for i in range(1, 16):
        for j in range(1, 16):
            temp = [g[i][j], g[i + 1][j + 1], g[i + 2][j + 2], g[i + 3][j + 3], g[i + 4][j + 4]]
            if temp == black_win:
                check = 1
                if [g[i - 1][j - 1]] + temp != [check] * 6 and temp + [g[i + 5][j + 5]] != [check] * 6:
                    win = check
                    print(win)
                    print(i, j)
                    break
            elif temp == white_win:
                check = 2
                if [g[i - 1][j - 1]] + temp != [check] * 6 and temp + [g[i + 5][j + 5]] != [check] * 6:
                    win = check
                    print(win)
                    print(i, j)
                    break
        if win != 0:
            break
    
    for i in range(5, 20):
        for j in range(1, 16):
            temp = [g[i][j], g[i - 1][j + 1], g[i - 2][j + 2], g[i - 3][j + 3], g[i - 4][j + 4]]
            if temp == black_win:
                check = 1
                if [g[i + 1][j - 1]] + temp != [check] * 6 and temp + [g[i - 5][j + 5]] != [check] * 6:
                    win = check
                    print(win)
                    print(i, j)
                    break
            elif temp == white_win:
                check = 2
                if [g[i + 1][j - 1]] + temp != [check] * 6 and temp + [g[i - 5][j + 5]] != [check] * 6:
                    win = check
                    print(win)
                    print(i, j)
                    break
        if win != 0:
            break


black_win = [1, 1, 1, 1, 1]
white_win = [2, 2, 2, 2, 2]

graph_r = [[0] * 21]
for _ in range(19):
    temp = list(map(int, input().split()))
    graph_r.append([0] + temp + [0])
graph_r.append([0] * 21)

graph_c = [[g[i] for g in graph_r] for i in range(21)]

win = 0
check_line(graph_r, 1)
if win == 0:
    check_line(graph_c, 2)
if win == 0:
    check_diag(graph_r)
if win == 0:
    print(0)