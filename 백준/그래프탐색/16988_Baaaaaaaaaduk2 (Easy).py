import sys
from collections import deque


def backtracking(cur, n, start):
    global answer
    
    if len(cur) == 2:
        temp = get_cnt(cur)
        answer = max(answer, temp)
        return
    
    for i in range(start, n):
        backtracking(cur + [i], n, i + 1)
    
    
def get_cnt(coord):
    cnt = 0
    visited = [[False for _ in range(M)] for _ in range(N)]
        
    x1, y1 = zero_points[coord[0]]
    x2, y2 = zero_points[coord[1]]
    
    board[x1][y1] = 1
    board[x2][y2] = 1
    
    for i in range(N):
        for j in range(M):
            if board[i][j] == 2 and not visited[i][j]:
                result, visited = bfs(board, i, j, visited)
                cnt += result
    
    board[x1][y1] = 0
    board[x2][y2] = 0
    
    return cnt


def bfs(board, x, y, visited):     
    flag = True
    result = 1
    
    visited[x][y] = True
    queue = deque()
    queue.append((x, y))
    
    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or nx > N - 1 or ny < 0 or ny > M - 1 or visited[nx][ny]:
                continue
            
            if board[nx][ny] == 2:
                queue.append((nx, ny))
                visited[nx][ny] = True
                result += 1
            elif board[nx][ny] == 1:
                visited[nx][ny] = True
            elif board[nx][ny] == 0:
                flag = False
    
    if flag:
        return result, visited
    else:
        return 0, visited
                
    
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

answer = 0

N, M = map(int, sys.stdin.readline().split())
board = []
zero_points = []
zero_cnt = 0

for i in range(N):
    temp = list(map(int, sys.stdin.readline().split()))
    for j in range(M):
        if temp[j] == 0:
            zero_points.append((i, j))
            zero_cnt += 1
    board.append(temp)

backtracking([], zero_cnt, 0)
print(answer)
