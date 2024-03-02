from collections import deque

def bfs(x, y):
    queue = deque([(x, y)])
    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx > 15 or ny < 0 or ny > 15:
                continue
            if graph[nx][ny] == 0:
                queue.append((nx, ny))
                graph[nx][ny] = 1
            elif graph[nx][ny] == 3:
                return 1
    return 0

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

T = 10
for _ in range(T):
    tc = int(input())
    graph = []
    for i in range(16):
        temp = list(map(int, input()))
        graph.append(temp)
        for j in range(16):
            if temp[j] == 2:
                start_x = i
                start_y = j
            if temp[j] == 3:
                end_x = i
                end_y = j

    print(f"#{tc} {bfs(start_x, start_y)}")