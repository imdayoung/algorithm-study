import sys
from collections import deque
sys.stdin = open("input.txt")


def bfs(x, y):
    queue = deque([(x, y)])
    queue2 = deque([(x, y)])
    visited = [[-1 for _ in range(n)] for _ in range(n)]
    visited[x][y] = 0

    # 벽을 깨지 않고 갈 수 있는 좌표 탐색
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx > n - 1 or ny < 0 or ny > n - 1:
                continue

            if visited[nx][ny] == -1 and room[nx][ny] == 1:
                queue.append((nx, ny))
                queue2.append((nx, ny))
                visited[nx][ny] = 0
    
    while queue2:
        x, y = queue2.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx > n - 1 or ny < 0 or ny > n - 1:
                continue
            
            if visited[nx][ny] == -1:
                if room[nx][ny] == 1:
                    queue2.append((nx, ny))
                    visited[nx][ny] = visited[x][y]
                else:
                    queue2.append((nx, ny))
                    visited[nx][ny] = visited[x][y] + 1
                
            else:
                if room[nx][ny] == 1:
                    visited[nx][ny] = min(visited[nx][ny], visited[x][y])
                else:
                    visited[nx][ny] = min(visited[nx][ny], visited[x][y] + 1)

    # for v in visited:
    #     print(v)

    return visited[-1][-1]

    
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

for _ in range(6):
    n = int(sys.stdin.readline())
    room = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(n)]

    print(bfs(0, 0))

# 2
# 0
# 3
# 18
# 0
# 0
# 