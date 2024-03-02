from collections import deque


def solution(maze):
    answer = 0
    
    return answer

maze = [[1, 0, 2], [0, 0, 0], [5, 0 ,5], [4, 0, 3]]
print("answer:", solution(maze))

# from collections import deque


# dx = [0, 0, 1, -1]
# dy = [1, -1, 0, 0]

# def bfs(x_r, y_r, x_b, y_b, graph, n, m):
#     queue = deque([(x_r, y_r, x_b, y_b)])
#     visited_r = [[False for _ in range(m)] for _ in range(n)]
#     visited_b = [[False for _ in range(m)] for _ in range(n)]
#     visited_r[x_r][y_r] = True
#     visited_b[x_b][y_b] = True
#     while queue:
#         x_r, y_r, x_b, y_b = queue.popleft()
#         print(x_r, y_r, x_b, y_b)
#         if graph[x_r][y_r] == 3 and graph[x_b][y_b] == 4:
#             print("도착한 듯")
#             return
#         for i in range(4):
#             nx_r = x_r + dx[i]
#             ny_r = y_r + dy[i]
#             if nx_r < 0 or nx_r > n - 1 or ny_r < 0 or ny_r > m - 1:
#                 continue
#             if graph[nx_r][ny_r] == 5 or graph[nx_r][ny_r] == 1 or visited_r[nx_r][ny_r]:
#                 continue
#             visited_r[nx_r][ny_r] = True
#             for j in range(4):
#                 nx_b = x_b + dx[j]
#                 ny_b = y_b + dy[j]
#                 if nx_b < 0 or nx_b > n - 1 or ny_b < 0 or ny_b > m - 1:
#                     continue
#                 if graph[nx_b][ny_b] == 5 or graph[nx_b][ny_b] == 2 or visited_b[nx_b][ny_b]:
#                     continue
#                 if nx_b == nx_r and ny_b == ny_r:
#                     continue
#                 visited_b[nx_b][ny_b] = True
#                 queue.append((nx_r, ny_r, nx_b, ny_b))
                

# def solution(maze):
#     answer = 0
#     n, m = len([m[0] for m in maze]), len(maze[0])
#     x_r, y_r, x_b, y_b = -1, -1, -1, -1
    
#     for i in range(n):
#         for j in range(m):
#             if maze[i][j] == 1:
#                 x_r, y_r = i, j
#             elif maze[i][j] == 2:
#                 x_b, y_b = i, j
    
#     # print(f"red: {x_r},{y_r} / blue: {x_b},{y_b}")
#     bfs(x_r, y_r, x_b, y_b, maze, n, m)
#     return answer

# maze = [[1, 0, 2], [0, 0, 0], [5, 0 ,5], [4, 0, 3]]
# solution(maze)