import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(x, y):
    global cnt
    visited[x][y] = True

    if graph[x][y] == "P":
        cnt += 1
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if -1 < nx < N and -1 < ny < M and not visited[nx][ny]:
            if graph[nx][ny] != "X":
                dfs(nx, ny)

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

cnt = 0
N, M = map(int, input().split())
graph = []
visited = [[False] * M for _ in range(N)]
for i in range(N):
    temp = list(map(str, input().rstrip()))
    graph.append(temp)
    for j in range(M):
        if temp[j] == "I":
            start_x = i
            start_y = j
            break

dfs(start_x, start_y)
if cnt == 0:
    print("TT")
else:
    print(cnt)