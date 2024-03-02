from collections import deque
import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

def bfs(x, y):
    queue = deque([(x, y)])
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx > M - 1 or ny < 0 or ny > N - 1:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                queue.append((nx, ny))
    return 1

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

T = int(input())
for _ in range(T):
    count = 0

    M, N, K = map(int, input().rstrip().split())
    graph = [[0] * N for _ in range(M)]

    for _ in range(K):
        X, Y = map(int, input().rstrip().split())
        graph[X][Y] = 1

    for i in range(M):
        for j in range(N):
            if graph[i][j] == 1:
                count += bfs(i, j)

    print(count)