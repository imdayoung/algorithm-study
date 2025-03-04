from collections import deque
from collections import defaultdict


graph = []
visited = []
cols = defaultdict(int)


def bfs(x, y, n, m):
    global visited
    size = 1
    col = set()
    col.add(y)
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    
    queue = deque([(x, y)])
    visited[x][y] = True
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx > n - 1 or ny < 0 or ny > m - 1:
                continue
            if not visited[nx][ny] and graph[nx][ny] == 1:
                size += 1
                col.add(ny)
                visited[nx][ny] = True
                queue.append((nx, ny))
    for c in col:
        cols[c] += size
    return size


def solution(land):
    global graph
    global visited

    n = len([l[0] for l in land])
    m = len(land[0])
    graph = land
    visited = [[False for _ in range(m)] for _ in range(n)]

    for i in range(n):
        for j in range(m):
            if not visited[i][j] and graph[i][j] == 1:
                bfs(i, j, n, m)

    return max(cols.values())


# 효율성 테스트 시간 초과
# from collections import deque


# def get_size(visited, graph, n, m, x, y):
#     queue = deque([(x, y)])
#     visited[x][y] = True
#     size = 1
    
#     while queue:
#         x, y = queue.popleft()
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
#             if nx < 0 or nx > n - 1 or ny < 0 or ny > m - 1:
#                 continue
#             if not visited[nx][ny] and graph[nx][ny] == 1:
#                 size += 1
#                 visited[nx][ny] = True
#                 queue.append((nx, ny))
#     return size

# dx = [0, 0, 1, -1]
# dy = [1, -1, 0, 0]

# def solution(land):
#     answer = 0
#     n = len([l[0] for l in land])
#     m = len(land[0])
    
#     for j in range(m):
#         temp = 0
#         visited = [[False for _ in range(m)] for _ in range(n)]
#         for i in range(n):
#             if not visited[i][j] and land[i][j] == 1:
#                 temp += get_size(visited, land, n, m, i, j)
#         answer = max(answer, temp)
            
#     return answer

# land = [[0, 0, 0, 1, 1, 1, 0, 0], [0, 0, 0, 0, 1, 1, 0, 0], [1, 1, 0, 0, 0, 1, 1, 0], [1, 1, 1, 0, 0, 0, 0, 0], [1, 1, 1, 0, 0, 0, 1, 1]]
# print(solution(land))