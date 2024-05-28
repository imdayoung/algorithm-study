import sys
    
    
def move(x, y):
    global amount
    global d
    while x != 0 or y != 0:
        for _ in range(amount):
            nx = x + dx[d]
            ny = y + dy[d]
            # print(f"[{x}][{y}]에서 [{nx}][{ny}]로 옮겨감")
            
            spread(nx, ny, tornado[x][y])
            
            x, y = nx, ny
            if x == 0 and y == 0:
                break
        d = (d + 1) % 4
        if d % 2 == 0:
            amount += 1
    
    
def spread(x, y, new_sand):
    global answer
    
    cur_sand = tornado[x][y]
    alpha = cur_sand
    for dx, dy, percentage in spread_list[d]:
        nx = x + dx
        ny = y + dy
        
        spreaded = int(cur_sand * percentage)
        # print(f"tornado[{nx}][{ny}]로 {cur_sand}가 {percentage} 비율로 퍼져서 총 {spreaded}만큼 퍼짐")
        alpha -= spreaded
        
        if nx < 0 or nx > N - 1 or ny < 0 or ny > N - 1:
            answer += spreaded
            continue
        tornado[nx][ny] += spreaded

    dx, dy = d_alpha[d]
    nx, ny = x + dx, y + dy
    if 0 <= nx <= N - 1 and 0 <= ny <= N - 1:
        tornado[nx][ny] += alpha
    else:
        answer += alpha
    tornado[x][y] = new_sand
    
    # print("==================== 퍼진 후 ====================")
    # for t in tornado:
    #     print(t)
    # print("================================================")
    

spread_list = [
    [(-1, 1, 0.01), (1, 1, 0.01), (-2, 0, 0.02), (2, 0, 0.02), (0, -2, 0.05), (-1, 0, 0.07), (1, 0, 0.07), (-1, -1, 0.1), (1, -1, 0.1)],
    [(-1, 1, 0.01), (-1, -1, 0.01), (0, -2, 0.02), (0, 2, 0.02), (2, 0, 0.05), (0, -1, 0.07), (0, 1, 0.07), (1, -1, 0.1), (1, 1, 0.1)],
    [(-1, -1, 0.01), (1, -1, 0.01), (-2, 0, 0.02), (2, 0, 0.02), (0, 2, 0.05), (-1, 0, 0.07), (1, 0, 0.07), (-1, 1, 0.1), (1, 1, 0.1)],
    [(1, 1, 0.01), (1, -1, 0.01), (0, -2, 0.02), (0, 2, 0.02), (-2, 0, 0.05), (0, -1, 0.07), (0, 1, 0.07), (-1, -1, 0.1), (-1, 1, 0.1)]
]
    
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]
d_alpha = [(0, -1), (1, 0), (0, 1), (-1, 0)]

answer = 0

d = 0
amount = 1

N = int(sys.stdin.readline())
tornado = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

cur_x, cur_y = N // 2, N // 2
move(cur_x, cur_y)
print(answer)
