import sys
from collections import deque


def move(x, y):
    queue = deque([(x, y)])
    
    visited = [[INF for _ in range(M)] for _ in range(N)]
    visited[x][y] = 0
    
    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx > N - 1 or ny < 0 or ny > M - 1:
                continue
            
            # 방문한 적 없는 곳
            if visited[nx][ny] == INF:
                visited[nx][ny] = visited[x][y] + graph[nx][ny]
                queue.append((nx, ny))
                
            # 방문했던 곳    
            else:
                if visited[x][y] + graph[nx][ny] < visited[nx][ny]:
                    visited[nx][ny] = visited[x][y] + graph[nx][ny]
                    queue.append((nx, ny))
            
    return visited
    
    
INF = int(1e9)

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

M, N = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(N)]
    
breaked_walls = move(0, 0)
print(breaked_walls[-1][-1])
