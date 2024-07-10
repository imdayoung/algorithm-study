import sys


answer = 0

N = int(sys.stdin.readline())

plans = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
plans.sort(key = lambda x:(x[0], x[0] - x[1]))
print(plans)

width, height = 0, 0
cur_start, cur_end = plans[0][0], plans[0][1]

for start, end in plans:
    # 밑으로 추가
    if start <= cur_end:
        width = end - cur_start
        height += 1
        cur_end = end

    # 옆으로 추가(이어지는 일정)
    elif start == cur_end - 1:
        
    
    # 옆으로 추가(이어지지 않음)
    else:
        answer += width * height
        width, height = 0, 0

print(answer)

# # 아 연속된 두 일자에 일정이 있으면 다 연속된거였음 ;; BFS가 아니었던 거임
# import sys
# from collections import deque


# def bfs(x, y):
#     queue = deque([(x, y)])
#     visited[x][y] = True
#     x_start, y_start = x, y
#     x_end, y_end = x_start, y_start
    
#     while queue:
#         x, y = queue.popleft()
#         for nx, ny in [(x + 1, y), (x, y + 1)]:
#             if nx < 0 or nx > N or ny < 0 or ny > plans[-1][1]:
#                 continue
            
#             if not visited[nx][ny] and graph[nx][ny] == 1:
#                 x_end = max(x_end, nx)
#                 y_end = max(y_end, ny)
#                 visited[nx][ny] = True
#                 queue.append((nx, ny))
           
#     result = (x_end - x_start + 1) * (y_end - y_start + 1)
#     return result
            

# answer = 0

# N = int(sys.stdin.readline())

# plans = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
# plans.sort(key = lambda x:(x[0], x[0] - x[1]))

# graph = [[0 for _ in range(plans[-1][1] + 1)] for _ in range(N + 1)]
# visited = [[False for _ in range(plans[-1][1] + 1)] for _ in range(N + 1)]

# for start, end in plans:
#     for i in range(N + 1):
#         if graph[i][start:end + 1] == [0 for _ in range(end - start + 1)]:
#             for j in range(start, end + 1):
#                 graph[i][j] = 1
#             break

# for g in graph:
#     print(g)

# for i in range(N + 1):
#     for j in range(plans[-1][1] + 1):
#         if not visited[i][j] and graph[i][j] == 1:
#             size = bfs(i, j)
#             answer += size

# print(answer)
