import copy
from collections import deque
import sys
input = sys.stdin.readline

def bfs():
    queue = deque()
    map_lab_temp = copy.deepcopy(map_lab)
    for i in range(N):
        for j in range(M):
            if map_lab_temp[i][j] == 2:
                queue.append((i, j))

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx > N - 1 or ny < 0 or ny > M - 1:
                continue
            if map_lab_temp[nx][ny] == 0:
                map_lab_temp[nx][ny] = 2
                queue.append((nx, ny))

    safe = 0
    for i in range(N):
        for j in range(M):
            if map_lab_temp[i][j] == 0:
                safe += 1
    return safe


dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def build_wall(cnt):
    global answer
    if cnt == 3:
        answer = max(answer, bfs())
        return

    for i in range(N):
        for j in range(M):
            if map_lab[i][j] == 0:
                map_lab[i][j] = 1
                build_wall(cnt + 1)
                map_lab[i][j] = 0


answer = 0
N, M = map(int, input().split())
map_lab = [list(map(int, input().split())) for _ in range(N)]
build_wall(0)
print(answer)