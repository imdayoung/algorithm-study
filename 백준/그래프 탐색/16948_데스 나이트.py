from collections import deque
import sys
input = sys.stdin.readline

def bfs(x, y):
    queue = deque([(x, y)])
    visited[x][y] = 0
    while queue:
        x, y = queue.popleft()
        if x == r2 and y == c2:
            return visited[x][y]
        
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx > N - 1 or ny < 0 or ny > N - 1:
                continue
            if visited[nx][ny] == -1:
                visited[nx][ny] = visited[x][y] + 1
                queue.append((nx, ny))
    return -1


dx = [-2, -2, 0, 0, 2, 2]
dy = [-1, 1, -2, 2, -1, 1]

N = int(input())
r1, c1, r2, c2 = map(int, input().split())
visited = [[-1] * N for _ in range(N)]

print(bfs(r1, c1))