from collections import deque
import sys
input = sys.stdin.readline


def rotate(x_start, x_end, y_start, y_end):
    queue = deque()
    x, y = x_start, y_start
    while y < y_end:
        queue.append(graph[x][y])
        y += 1
    while x < x_end:
        queue.append(graph[x][y])
        x += 1
    while y > y_start:
        queue.append(graph[x][y])
        y -= 1
    while x > x_start:
        queue.append(graph[x][y])
        x -= 1

    queue.append(queue.popleft())
    
    x, y = x_start, y_start
    while y < y_end:
        graph[x][y] = queue.popleft()
        y += 1
    while x < x_end:
        graph[x][y] = queue.popleft()
        x += 1
    while y > y_start:
        graph[x][y] = queue.popleft()
        y -= 1
    while x > x_start:
        graph[x][y] = queue.popleft()
        x -= 1


N, M, R = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

for _ in range(R):
    x_start, x_end = 0, N - 1
    y_start, y_end = 0, M - 1
    for _ in range(min(N, M) // 2):
        rotate(x_start, x_end, y_start, y_end)
        x_start += 1
        x_end -= 1
        y_start += 1
        y_end -= 1

for g in graph:
    print(*g)