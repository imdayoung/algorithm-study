from collections import deque
import sys
input = sys.stdin.readline


def bfs(x, y, rain):
    queue = deque([(x, y)])
    visited[x][y] = True

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx > N - 1 or ny < 0 or ny > N - 1:
                continue
            if ground[nx][ny] <= rain:
                continue
            if ground[nx][ny] > rain and not visited[nx][ny]:
                visited[nx][ny] = True
                queue.append((nx, ny))
                

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

answer = 1

N = int(input())
ground = []
min_value = 100
max_value = 1

for _ in range(N):
    temp = list(map(int, input().split()))
    for i in range(N):
        if temp[i] < min_value:
            min_value = temp[i]
        elif temp[i] > max_value:
            max_value = temp[i]
    ground.append(temp)

for k in range(min_value, max_value):
    cnt = 0
    visited = [[False] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if ground[i][j] > k and not visited[i][j]:
                bfs(i, j, k)
                cnt += 1
    if cnt >= answer:
        answer = cnt
    
print(answer)