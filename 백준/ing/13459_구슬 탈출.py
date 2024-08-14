import sys
from collections import deque


def bfs(rx, ry, bx, by):
    queue = deque([(rx, ry, bx, by)])
    
    
    while queue:
        rx, ry, bx, by = queue.popleft()
        for i in range(4):
            nrx = rx + dx[i]
            nry = ry + dy[i]
            nbx = bx + dx[i]
            nby = by + dy[i]
            
        if board[nrx][nry] == '#':
            nrx, nry = rx, ry
        if board[nbx][nby] == '#':
            nbx, nby = bx, by
            
        
            
    return 0


dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

N, M = map(int, sys.stdin.readline().split())

red_x, red_y =  0, 0
blue_x, blue_y = 0, 0

board = []
for i in range(N):
    temp = list(map(str, sys.stdin.readline().rstrip()))
    for j in range(M):
        if temp[j] == 'A':
            red_x, red_y = i, j
        elif temp[j] == 'B':
            blue_x, blue_y = i, j
            
    board.append(temp)
    
answer = bfs(red_x, red_y, blue_x, blue_y)
print(answer)
