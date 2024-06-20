import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000) #python이 정한 최대 깊이를 더 깊게 변경해줌

def dfs(v):
    visited[v] = True
    components.remove(v)
    for i in graph[v]:
        if not visited[i]:
            dfs(i)

# 정점의 개수 n, 간선의 개수 m
n, m = map(int, input().rstrip().split())

graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
components = [i for i in range(1, n + 1)]
start = 1
answer = 0

for _ in range(m):
    u, v = map(int, input().rstrip().split())
    graph[u].append(v)
    graph[v].append(u)

while components:
    dfs(start)
    answer += 1
    if not components:
        break
    start = components[0]

print(answer)