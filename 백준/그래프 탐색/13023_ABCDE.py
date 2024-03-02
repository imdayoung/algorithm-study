import sys
input = sys.stdin.readline


def dfs(x, cnt):
    global answer
    if cnt == 4:
        answer = 1
        return

    visited[x] = True
    for nx in graph[x]:
        if not visited[nx]:
            dfs(nx, cnt + 1)
            visited[nx] = False
            

answer = 0
N, M = map(int, input().split())
graph = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * N
for i in range(N):
    dfs(i, 0)
    visited[i] = False
    if answer == 1:
        break

print(answer)