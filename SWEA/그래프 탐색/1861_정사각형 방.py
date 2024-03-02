from collections import deque

def bfs(x, y):
    cnt = 0
    queue = deque([(x, y)])
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx > N - 1 or ny < 0 or ny > N - 1:
                continue
            if graph[nx][ny] == graph[x][y] + 1:
                cnt += 1
                queue.append((nx, ny))
    return cnt

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

T = int(input())
for tc in range(1, T + 1):
    answer = []
    max_cnt = 0

    N = int(input())
    graph = [list(map(int, input().split())) for _ in range(N)]
    
    for i in range(N):
        for j in range(N):
            temp = bfs(i, j)
            if temp > max_cnt:
                answer = [graph[i][j]]
                max_cnt = temp
            elif temp == max_cnt:
                answer.append(graph[i][j])

    print(f"#{tc} {min(answer)} {max_cnt + 1}")