import sys
input = sys.stdin.readline

def div(n, x, y):
    global white
    global blue
    flag = 0
    check = paper[x][y]
    for i in range(x, x + n):
        for j in range(y, y + n):
            if paper[i][j] != check:
                flag = -1
                break
        if flag == -1:
            break

    if flag == -1:
        n //= 2
        div(n, x, y)
        div(n, x + n, y)
        div(n, x, y + n)
        div(n, x + n, y + n)

    else:
        if check == 0:
            white += 1
        elif check == 1:
            blue += 1


N = int(input())
paper = [list(map(int, input().split())) for _ in range(N)]
white, blue = 0, 0
div(N, 0, 0)

print(white)
print(blue)