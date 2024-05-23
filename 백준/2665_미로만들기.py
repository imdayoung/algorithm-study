import sys
from collections import deque

# dp ,,,,,,,,,,,,,,,,,,,,,?????????
def bfs(x, y):
    queue = deque([(x, y)])
    visited = [[0 for _ in range(n)] for _ in range(n)]
    
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx > n - 1 or ny < 0 or ny > n - 1:
                continue
            # 음
            # if not visited[nx][ny] and room[nx][ny] == 1:
                

    
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

n = int(sys.stdin.readline())
room = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(n)]

bfs(0, 0)
