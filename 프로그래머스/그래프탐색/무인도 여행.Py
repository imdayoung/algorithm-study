from collections import deque


dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def solution(maps):
    def bfs(x, y):
        result = int(maps[x][y])

        queue = deque([(x, y)])
        visited[x][y] = True

        while queue:
            x, y = queue.popleft()

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if nx < 0 or nx > n - 1 or ny < 0 or ny > m - 1 or visited[nx][ny]:
                    continue

                visited[nx][ny] = True
                if maps[nx][ny] != 'X':
                    queue.append((nx, ny))
                    result += int(maps[nx][ny])

        return result
    
    
    answer = []
    
    n = len(maps)
    m = len(maps[0])
    visited = [[False for _ in range(m)] for _ in range(n)]
    
    for i in range(n):
        for j in range(m):
            if not visited[i][j] and maps[i][j] != 'X':
                result = bfs(i, j)
                answer.append(result)

    if len(answer) == 0:
        answer = [-1]
    else:
        answer.sort()
        
    return answer