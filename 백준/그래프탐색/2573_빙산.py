import sys
from collections import deque


def bfs(x, y):
    queue = deque([(x, y)])
    visited[x][y] = True
    next_glacier = []

    while queue:
        x, y = queue.popleft()
        zeros = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx > N - 1 or ny < 0 or ny > M - 1:
                continue

            if glacier[nx][ny] != 0 and not visited[nx][ny]:
                visited[nx][ny] = True
                queue.append((nx, ny))

            elif glacier[nx][ny] == 0:
                zeros += 1

        next_glacier.append((x, y, max(glacier[x][y] - zeros, 0)))
    
    for x, y, remain in next_glacier:
        glacier[x][y] = remain


dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

answer = 0

N, M = map(int, sys.stdin.readline().split())
glacier = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

cnt = 0
while True:
    visited = [[False for _ in range(M)] for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if glacier[i][j] != 0 and not visited[i][j]:
                bfs(i, j)
                cnt += 1

    if cnt == 0:
        answer = 0
        break

    if cnt != 1:
        break

    cnt = 0
    answer += 1

print(answer)