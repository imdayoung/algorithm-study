# 엥 벽부수고 이동하기랑 똑같은 거 아닌가 까먹음 ;;
import sys
from collections import deque


def move():
    queue = deque([(0, 0)])
    visited = [[[0 for _ in range(M)] for _ in range(N)] for _ in range(2)]
    
    while queue:
        x, y, z = queue.popleft()
        if x == N - 1 and y == M - 1:
            return z
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx > N - 1 or ny < 0 or ny > M - 1:
                continue
            
            # if graph[nx][ny] == 1 :
                
            
    return -1
    

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

M, N = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(N)]

for g in graph:
    print(g)
    
answer = move()
print(answer)