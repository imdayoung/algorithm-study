from collections import deque
import sys


def bfs(x, y):
    size = 1
    queue = deque([(x, y)])
    visited[x][y] = True
    graph[x][y] = 0
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx > N or ny < 0 or ny > M:
                continue
            if not visited[nx][ny] and graph[nx][ny] == 1:
                size += 1
                visited[nx][ny] = True
                graph[nx][ny] = 0
                queue.append((nx, ny))
    return size


dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

N, M, K = map(int, sys.stdin.readline().split())
graph = [[0 for _ in range(M + 1)] for _ in range(N + 1)]
visited = [[False for _ in range(M + 1)] for _ in range(N + 1)]

for _ in range(K):
    r, c = map(int, sys.stdin.readline().split())
    graph[r][c] = 1

answer = 0
for i in range(N + 1):
    for j in range(M + 1):
        if graph[i][j] == 1:
            answer = max(answer, bfs(i, j))

print(answer)