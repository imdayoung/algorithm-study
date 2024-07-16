import sys
from collections import deque
sys.stdin = open("input.txt")


def check_removable(x, y, color):
    result = False
    
    queue = deque([(x, y)])
    visited = [[False for _ in range(m)] for _ in range(n)]
    
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx > n - 1 or ny < 0 or ny > m - 1:
                continue
            if not visited[nx][ny] and 
            
    
    return result

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

n, m = 12, 6
last = ['.' for _ in range(m)]

board = [list(map(str, sys.stdin.readline().rstrip())) for _ in range(n)]

for i in range(n - 1, -1, -1):
    if board[i] == last:
        break
    for j in range(m):
        check_removable(i, j)
        