from collections import deque
import sys
input = sys.stdin.readline


def bfs(x, y):
    queue = deque([(x, y)])
    visited[x][y] = 0

    while queue:
        x, y = queue.popleft()
        if x == target_x and y == target_y:
            return visited[x][y]

        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx > I - 1 or ny < 0 or ny > I - 1:
                continue
            if visited[nx][ny] == -1:
                visited[nx][ny] = visited[x][y] + 1
                queue.append((nx, ny))


dx = [-2, -2, -1, -1, 1, 1, 2, 2]
dy = [-1, 1, -2, 2, -2, 2, -1, 1]

T = int(input())
for _ in range(T):
    I = int(input())
    now_x, now_y = map(int, input().split())
    target_x, target_y = map(int, input().split())
    board = [[0] * I for _ in range(I)]
    visited = [[-1] * I for _ in range(I)]
    print(bfs(now_x, now_y))