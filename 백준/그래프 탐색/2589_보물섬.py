from collections import deque
import sys
input = sys.stdin.readline

def bfs(x, y):
    queue = deque([(x, y)])
    visited[x][y] = 0
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx > n - 1 or ny < 0 or ny > m - 1 or board[nx][ny] == "W":
                continue
            if visited[nx][ny] == -1 and board[nx][ny] == "L":
                visited[nx][ny] = visited[x][y] + 1
                queue.append((nx, ny))
        temp = visited[x][y]
    return temp


dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

n, m = map(int, input().split())
board = [list(map(str, input().rstrip())) for _ in range(n)]

answer = 0
for i in range(n):
    for j in range(m):
        if board[i][j] == "L":
            visited = [[-1] * m for _ in range(n)]
            answer = max(answer, bfs(i, j))

print(answer)