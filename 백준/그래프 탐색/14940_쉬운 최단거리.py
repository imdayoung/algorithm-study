# #1
# 4 3 2 1 0
# 0 0 0 0 0
# #2
# 0 0
# 0 0
# #3
# 0 0 -1
# 0 -1 -1
# -1 -1 -1

from collections import deque
import sys
input = sys.stdin.readline

def bfs(x, y):
    queue = deque([(x, y)])
    visited[x][y] = True
    result[x][y] = 0

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx > n - 1 or ny < 0 or ny > m - 1:
                continue

            if not visited[nx][ny]:
                if graph[nx][ny] == 1:
                    visited[nx][ny] = True
                    result[nx][ny] = result[x][y] + 1
                    queue.append((nx, ny))


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 세로 n, 가로 m
n, m = map(int, input().split())
target_x, target_y = 0, 0

graph = []
visited = [[False] * m for _ in range(n)]
result = [[-1] * m for _ in range(n)]
for i in range(n):
    temp = list(map(int, input().split()))
    graph.append(temp)
    for j in range(m):
        if temp[j] == 2:
            target_x = i
            target_y = j

bfs(target_x, target_y)

for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            result[i][j] = 0

for r in result:
    print(*r)


# from collections import deque
# import sys
# input = sys.stdin.readline

# def bfs(x, y):
#     queue = deque()
#     queue.append([x, y])
#     visited[x][y] = 0

#     while queue:
#         x, y = queue.popleft()

#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
#             if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == -1:
#                 if graph[nx][ny] == 0:
#                     visited[nx][ny] = 0
#                 elif graph[nx][ny] == 1:
#                     visited[nx][ny] = visited[x][y] + 1
#                     queue.append([nx, ny])

# n, m = map(int, input().rstrip().split())
# graph = [list(map(int, input().rstrip().split())) for _ in range(n)]
# visited = [[-1] * m for _ in range(n)]
# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]

# for i in range(n):
#     for j in range(m):
#         if graph[i][j] == 2 and visited[i][j] == -1:
#             bfs(i, j)

# for i in range(n):
#     for j in range(m):
#         if graph[i][j] == 0:
#             print(0, end = " ")
#         else:
#             print(visited[i][j], end = " ")
#     print()


