from collections import deque
import sys


def bfs(graph, visited, x, y, z):
    queue = deque([(x, y, z)])
    visited[x][y][z] = 0

    while queue:
        x, y, z = queue.popleft()        
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]

            if nx < 0 or nx > L - 1 or ny < 0 or ny > R - 1 or nz < 0 or nz > C - 1:
                continue

            if visited[nx][ny][nz] == -1 and graph[nx][ny][nz] == ".":
                visited[nx][ny][nz] = visited[x][y][z] + 1
                queue.append((nx, ny, nz))

            if graph[nx][ny][nz] == "E":
                return visited[x][y][z] + 1
    
    return 0

answers = []
dx = [0, 0, 0, 0, 1, -1]
dy = [0, 0, 1, -1, 0, 0]
dz = [1, -1, 0, 0, 0, 0]

L, R, C = map(int, sys.stdin.readline().split())
while L != 0 or R != 0 or C != 0:
    time = 0

    building = [[0 for _ in range(R)] for _ in range(L)]
    visited = [[[-1 for _ in range(C)] for _ in range(R)] for _ in range(L)]
    start_x, start_y, start_z = -1, -1, -1

    for i in range(L):
        for j in range(R):
            building[i][j] = list(map(str, sys.stdin.readline().rstrip()))
            if start_x == -1:
                for k in range(C):
                    if building[i][j][k] == "S":
                        start_x, start_y, start_z = i, j, k
                        break
        sys.stdin.readline()

    answers.append(bfs(building, visited, start_x, start_y, start_z))
    L, R, C = map(int, sys.stdin.readline().split())


for answer in answers:
    if answer == 0:
        print("Trapped!")
    else:
        print(f"Escaped in {answer} minute(s).")