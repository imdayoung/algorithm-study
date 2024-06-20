import sys
from collections import deque


def bfs(x, y, z):
    # x좌표, y좌표, 벽 부순 횟수
    queue = deque([(x, y, z)])
    visited = [[[-1 for _ in range(2)] for _ in range(M)] for _ in range(N)]
    visited[x][y][0] = 0

    while queue:
        x, y, z = queue.popleft()
        if x == Ex - 1 and y == Ey - 1:
            return visited[x][y][z]
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx > N - 1 or ny < 0 or ny > M - 1:
                continue
                
            if graph[nx][ny] == 0 and visited[nx][ny][z] == -1:
                visited[nx][ny][z] = visited[x][y][z] + 1
                queue.append((nx, ny, z))

            elif graph[nx][ny] == 1 and z == 0:
                visited[nx][ny][1] = visited[x][y][0] + 1
                queue.append((nx, ny, 1))
            
    return -1


dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

N, M = map(int, sys.stdin.readline().split())
Hx, Hy = map(int, sys.stdin.readline().split())
Ex, Ey = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

print(bfs(Hx - 1, Hy - 1, 0))