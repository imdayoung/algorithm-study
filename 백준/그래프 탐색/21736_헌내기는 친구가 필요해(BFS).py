from collections import deque
import sys
input = sys.stdin.readline

def bfs(x, y):
    queue = deque([(x, y)])
    visited = [[False] * M for _ in range(N)]
    visited[x][y] = True
    cnt = 0
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx > N - 1 or ny < 0 or ny > M - 1:
                continue
            if graph[nx][ny] == "X":
                visited[nx][ny] = True
                continue
            if not visited[nx][ny]:
                visited[nx][ny] = True
                if graph[nx][ny] == "P":
                    cnt += 1
                queue.append((nx, ny))
    return cnt

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

N, M = map(int, input().split())
graph = []
for i in range(N):
    temp = list(map(str, input().rstrip()))
    graph.append(temp)
    for j in range(M):
        if temp[j] == "I":
            start_x = i
            start_y = j
            break

answer = bfs(start_x, start_y)
if answer == 0:
    print("TT")
else:
    print(answer)