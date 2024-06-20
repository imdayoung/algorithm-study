from collections import deque
import sys
input = sys.stdin.readline

def bfs(x, y):
    move = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    queue = deque([(x, y)])

    while queue:
        x, y = queue.popleft()
        if x == N - 1 and y == M - 1:
            return graph[x][y]

        for dx, dy in move:
            nx = x + dx
            ny = y + dy
            if nx < 0 or ny < 0 or nx >= N or ny >= M:
                continue
            if graph[nx][ny] == 0:
                continue
            
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))

N, M = map(int, input().split())
graph = [list(map(int, input().rstrip())) for _ in range(N)]
print(bfs(0, 0))