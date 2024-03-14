from collections import deque
import sys


def bfs(x, y):
    global total_sheep
    global total_wolf

    queue = deque([(x, y)])
    visited[x][y] = True

    in_sheep, in_wolf = 0, 0
    if yard[x][y] == 'o':
        in_sheep += 1
    elif yard[x][y] == 'v':
        in_wolf += 1

    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx > R - 1 or ny < 0 or ny > C - 1 or visited[nx][ny]:
                continue
            if yard[nx][ny] == 'o':
                in_sheep += 1
            elif yard[nx][ny] == 'v':
                in_wolf += 1
            visited[nx][ny] = True
            queue.append((nx, ny))

    if in_sheep > in_wolf:
        total_wolf -= in_wolf
    else:
        total_sheep -= in_sheep


dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

R, C = map(int, sys.stdin.readline().split())
yard = [list(map(str, sys.stdin.readline().rstrip())) for _ in range(R)]
visited = [[False for _ in range(C)] for _ in range(R)]

total_sheep, total_wolf = 0, 0
for i in range(R):
    for j in range(C):
        if yard[i][j] == 'o':
            total_sheep += 1
        elif yard[i][j] == 'v':
            total_wolf += 1
        elif yard[i][j] == '#':
            visited[i][j] = True
            
for i in range(R):
    for j in range(C):
        if not visited[i][j]:
            bfs(i, j)

print(total_sheep, total_wolf)