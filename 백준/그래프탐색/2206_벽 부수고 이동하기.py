from collections import deque
import sys
input = sys.stdin.readline


def bfs(x, y, z):
    queue = deque([(x, y, z)]) # x, y, braek 횟수

    while queue:
        x, y, z = queue.popleft()
        if x == N - 1 and y == M - 1:
            return visited[x][y][z]
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx > N - 1 or ny < 0 or ny > M - 1:
                continue

            if board[nx][ny] == 1 and z == 0:
                visited[nx][ny][1] = visited[x][y][0] + 1
                queue.append((nx, ny, 1))
            elif board[nx][ny] == 0 and visited[nx][ny][z] == 0:
                visited[nx][ny][z] = visited[x][y][z] + 1
                queue.append((nx, ny, z))
    return -1


dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

N, M = map(int, input().split())
board = [list(map(int, input().rstrip())) for _ in range(N)]
for b in board:
    print(b)
visited = [[[0] * 2 for _ in range(M)] for _ in range(N)]
visited[0][0][0] = 1
for v in visited:
    print(v)
print(bfs(0, 0, 0))