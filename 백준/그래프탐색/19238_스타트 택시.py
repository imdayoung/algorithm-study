import sys
from collections import deque


# 다음에 태울 손님의 현재 위치와 거리 return
def getNextConsumer(start_x, start_y):
    queue = deque([(start_x, start_y)])
    visited = [[-1 for _ in range(N)] for _ in range(N)]
    visited[start_x][start_y] = 0
    candidates = []
    
    while queue:
        x, y = queue.popleft()
        if board[x][y] > 1:
            candidates.append((x, y, visited[x][y]))
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or nx > N - 1 or ny < 0 or ny > N - 1:
                continue
            
            if board[nx][ny] != 1 and visited[nx][ny] == -1:
                queue.append((nx, ny))
                visited[nx][ny] = visited[x][y] + 1
                
    if len(candidates) == 0:
        return -1, -1, -1
    
    candidates.sort(key = lambda x:(x[2], x[0], x[1]))
    return candidates[0][0], candidates[0][1], candidates[0][2]
    
    
# 목적지에 도달하기 위해 필요한 연료 return
def drive(start_x, start_y, target_x, target_y):
    queue = deque([(start_x, start_y)])
    visited = [[-1 for _ in range(N)] for _ in range(N)]
    visited[start_x][start_y] = 0
    
    while queue:
        x, y = queue.popleft()
        if x == target_x and y == target_y:
            return visited[x][y]
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or nx > N - 1 or ny < 0 or ny > N - 1:
                continue
            
            if board[nx][ny] != 1 and visited[nx][ny] == -1:
                queue.append((nx, ny))
                visited[nx][ny] = visited[x][y] + 1
            
    return -1
            
    
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

destinations = []

N, M, fuel = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
taxi_x, taxi_y = map(int, sys.stdin.readline().split())
taxi_x -= 1
taxi_y -= 1
for i in range(M):
    src_x, src_y, dest_x, dest_y = map(int, sys.stdin.readline().split())
    destinations.append((dest_x - 1, dest_y - 1))
    board[src_x - 1][src_y - 1] = i + 2
    
for _ in range(M):
    x, y, dist = getNextConsumer(taxi_x, taxi_y)
    if x == -1 or dist > fuel:
        answer = -1
        break
    
    taxi_x, taxi_y = x, y
    fuel -= dist
    consume = drive(taxi_x, taxi_y, destinations[board[x][y] - 2][0], destinations[board[x][y] - 2][1])
    
    if consume == -1 or consume > fuel:
        answer = -1
        break
    
    fuel += consume
    
    taxi_x, taxi_y = destinations[board[x][y] - 2][0], destinations[board[x][y] - 2][1]
    board[x][y] = 0
    answer = fuel
    
print(answer)