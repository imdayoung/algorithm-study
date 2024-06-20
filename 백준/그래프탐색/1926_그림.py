from collections import deque
import sys
input = sys.stdin.readline


def bfs(x, y):
    size = 1
    queue = deque([(x, y)])
    visited[x][y] = True
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx > n - 1 or ny < 0 or ny > m - 1 or paint[nx][ny] == 0:
                continue
            if not visited[nx][ny] and paint[nx][ny] == 1:
                visited[nx][ny] = True
                queue.append((nx, ny))
                size += 1
    return size


dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

answer_count = 0
answer_max_size = 0
n, m = map(int, input().split())
paint = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
for i in range(n):
    for j in range(m):
        if not visited[i][j] and paint[i][j] == 1:
            answer_count += 1
            answer_max_size = max(answer_max_size, bfs(i, j))

print(answer_count)
print(answer_max_size)