from collections import deque
import sys
input = sys.stdin.readline

def bfs(x, y):
    queue = deque([(x, y)])
    visited[x][y] = True
    size = 1

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx > N - 1 or ny < 0 or ny > M- 1:
                continue
            if board[nx][ny] == 0:
                continue
            if board[nx][ny] == 1 and not visited[nx][ny]:
                visited[nx][ny] = True
                queue.append((nx, ny))
                size += 1
    return size
        

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

cnt = 0
sizes = []
M, N, K = map(int, input().split())
board = [[1] * M for _ in range(N)]
visited = [[False] * M for _ in range(N)]
for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(x1, x2):
        for j in range(y1, y2):
            board[i][j] = 0

for i in range(N):
    for j in range(M):
        if board[i][j] == 1 and not visited[i][j]:
            sizes.append(bfs(i, j))
            cnt += 1

sizes.sort()
print(cnt)
print(*sizes)