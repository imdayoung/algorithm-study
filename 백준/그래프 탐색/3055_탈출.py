from collections import deque
import sys


def water_spread():
    global queue_water
    water_size = len(queue_water)

    for _ in range(water_size):
        x, y = queue_water.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx > R - 1 or ny < 0 or ny > C - 1:
                continue
            if graph[nx][ny] == 'D' or graph[nx][ny] == 'X' or graph[nx][ny] == '*':
                continue
            graph[nx][ny] = '*'
            queue_water.append((nx, ny))


def move(x, y):
    queue = deque([(x, y)])
    while queue:
        queue_size = len(queue)
        water_spread()
        for _ in range(queue_size):
            x, y = queue.popleft()
            
            if graph[x][y] == 'D':
                return visited[x][y]
            
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if nx < 0 or nx > R - 1 or ny < 0 or ny > C - 1:
                    continue
                if graph[nx][ny] == 'X' or graph[nx][ny] == '*':
                    continue
                if visited[nx][ny] == 0:
                    visited[nx][ny] = visited[x][y] + 1
                    queue.append((nx, ny))

    return "KAKTUS"


dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

R, C = map(int, sys.stdin.readline().split())
graph = []
x_start, x_end = 0, 0
queue_water = deque()
visited = [[0 for _ in range(C)] for _ in range(R)]

for i in range(R):
    temp = list(map(str, input().rstrip()))
    for j in range(C):
        if temp[j] == 'S':
            x_start, x_end = i, j
        elif temp[j] == '*':
            queue_water.append((i, j))
    graph.append(temp)

print(move(x_start, x_end))