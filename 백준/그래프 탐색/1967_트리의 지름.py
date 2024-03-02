import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)


def dfs(v, c, standard):
    global distance
    global start_node

    visited[v] = True
    if len(graph[v]) == 1 and v!= standard:
        if c > distance:
            distance = c
            start_node = v
        return
    for nv, cost in graph[v]:
        if not visited[nv]:
            dfs(nv, c + cost, standard)


n = int(input())
graph = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

distance = 0
start_node = 0
visited = [False] * (n + 1)
dfs(1, 0, 1)

distance = 0
visited = [False] * (n + 1)
dfs(start_node, 0, start_node)

print(distance)