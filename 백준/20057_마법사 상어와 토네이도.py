import sys


def move(x, y):
    # ㅇㅏ ,,,,,,,,,,,,,
    global d
    global amount
    
    d = (d + 1) % 4
    if d % 2 == 0:
        amount += 1
    
    nx, ny = x + dx[d], y + dy[d]
    return nx, ny
    
    
def spread(x, y, new_sand):
    print("spread")
    
    cur_sand = tornado[x][y]
    alpha = cur_sand
    for dx, dy, percentage in spread_list[d]:
        nx = x + dx
        ny = y + dy
        spreaded = int(cur_sand * percentage)
        alpha -= spreaded
        
        if nx < 0 or nx > N - 1 or ny < 0 or ny > N - 1:
            continue
        tornado[nx][ny] += spreaded

    dx, dy = d_alpha[d]
    nx, ny = x + dx, y + dy
    if 0 <= nx <= N - 1 and 0 <= ny <= N - 1:
        tornado[nx][ny] = alpha
    tornado[x][y] = new_sand
    
    for t in tornado:
        print(t)
    
    
spread_list = [
    [(-1, 1, 0.01), (1, 1, 0.01), (-2, 0, 0.02), (2, 0, 0.02), (0, -2, 0.05), (-1, 0, 0.07), (1, 0, 0.07), (-1, -1, 0.1), (1, -1, 0.1)],
    [(-1, 1, 0.01), (-1, -1, 0.01), (0, -2, 0.02), (0, 2, 0.02), (2, 0, 0.05), (0, -1, 0.07), (0, 1, 0.07), (1, -1, 0.1), (1, 1, 0.1)],
    [(-1, -1, 0.01), (1, -1, 0.01), (-2, 0, 0.02), (2, 0, 0.02), (0, 2, 0.05), (-1, 0, 0.07), (1, 0, 0.07), (-1, 1, 0.1), (1, 1, 0.1)],
    [(1, 1, 0.01), (1, -1, 0.01), (0, -2, 0.02), (0, 2, 0.02), (-2, 0, 0.05), (0, -1, 0.07), (0, 1, 0.07), (-1, -1, 0.1), (-1, 1, 0.1)]
]
    
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]
d_alpha = [(0, -1), (1, 0), (0, 1), (-1, 0)]

d = -1
amount = 0

N = int(sys.stdin.readline())
tornado = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

cur_x, cur_y = N // 2, N // 2

while cur_x != 1 or cur_y != 1:
    next_x, next_y = move(cur_x, cur_y)
    print(next_x, next_y)
    spread(next_x, next_y, tornado[cur_x][cur_y])
    cur_x, cur_y = next_x, next_y
