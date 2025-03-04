from collections import deque

def solution(maps):
    def bfs(x, y):
        cnt = 0
        queue = deque([(x, y)])
        visited = [[0] * m for _ in range(n)]
        visited[x][y] = 1
        
        while queue:
            x, y = queue.popleft()
            if x == n - 1 and y == m - 1:
                return visited[x][y]
            
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx < 0 or nx > n - 1 or ny < 0 or ny > m - 1 or maps[nx][ny] == 0:
                    continue
                if not visited[nx][ny] and maps[nx][ny] == 1:
                    visited[nx][ny] = visited[x][y] + 1
                    queue.append((nx, ny))
        return -1

    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]
    n = len([m[0] for m in maps])
    m = len(maps[0])
    return bfs(0, 0)