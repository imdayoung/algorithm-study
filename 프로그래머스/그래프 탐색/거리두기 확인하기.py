from collections import deque


dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def bfs(graph, x, y):
    visited = [[-1 for _ in range(5)] for _ in range(5)]
    visited[x][y] = 0
    queue = deque([(x, y)])

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if visited[x][y] > 1:
                continue
            if nx < 0 or nx > 4 or ny < 0 or ny > 4:
                continue
            if graph[nx][ny] == 'X':
                continue
            if visited[nx][ny] == -1 and graph[nx][ny] == 'O':
                visited[nx][ny] = visited[x][y] + 1
                queue.append((nx, ny))
            if visited[nx][ny] == -1 and graph[nx][ny] == 'P':
                print(nx, ny)
                return 0
            
    return 1



def solution(places):
    answer = []
    
    for place in places:
        temp = -1
        for x in range(5):
            for y in range(5):
                if place[x][y] == 'P':
                    temp = bfs(place, x, y)
                    if temp == 0:
                       answer.append(0)
                       break
            if temp == 0:
                break
        else:
            answer.append(1)

    return answer