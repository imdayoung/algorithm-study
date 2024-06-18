import sys
from collections import deque
sys.stdin = open("input.txt")


def bfs(x, y):
    right, bottom = 0, 0
    queue = deque([(x, y)])
    visited[x][y] = True
    
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx > max_width - 1 or ny < 0 or ny > max_height:
                continue
            if not visited[nx][ny]:
                visited[nx][ny] = True
                
    return right - x + 1, bottom - y + 1
            
        
answer = 0

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

width = 14
height = 10
N = int(sys.stdin.readline())
plans = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
plans.sort(key = lambda x : (x[0], -x[1]))

board = [[0 for _ in range(width + 1)] for _ in range(height)]

max_width = 0
max_height = 0

for start, end in plans:
    max_width = end + 1
    for i in range(10):
        if board[i][start] == 0:
            max_height = max(max_height, i + 1)
            for j in range(start, end + 1):
                board[i][j] = 1
            break
        
print(max_width, max_height)
for b in board:
    print(b)
    
visited = [[False for _ in range(max_width + 1)] for _ in range(max_height)]
# for i in range(max_width + 1):
#     for j in range(max_height):
#         if board[i][j] == 1:
#             w, h = bfs(i, j)
#             answer += w * h
