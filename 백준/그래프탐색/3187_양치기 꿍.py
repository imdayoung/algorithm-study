import sys
from collections import deque


def bfs(x, y, s, w):
    queue = deque([(x, y)])
    visited[x][y] = True
    sheep, wolf = s, w

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx > R - 1 or ny < 0 or ny > C - 1:
                continue
            if field[nx][ny] == '#':
                continue
            if not visited[nx][ny]:
                visited[nx][ny] = True
                queue.append((nx, ny))
                if field[nx][ny] == 'v':
                    wolf += 1
                elif field[nx][ny] == 'k':
                    sheep += 1
    
    if sheep > wolf:
        return sheep, 0
    else:
        return 0, wolf


sheeps, wolves = 0, 0

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

R, C = map(int, sys.stdin.readline().split())
field = [list(map(str, sys.stdin.readline())) for _ in range(R)]
visited = [[False for _ in range(C)] for _ in range(R)]

for i in range(R):
    for j in range(C):
        if not visited[i][j]:
            if field[i][j] == 'v':
                s, w = bfs(i, j, 0, 1)
            elif field[i][j] == 'k':
                s, w = bfs(i, j, 1, 0)
            else:
                s, w = 0, 0
                
            sheeps += s
            wolves += w
        
print(sheeps, wolves)