import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

ans = []

def dfs(v):
    visited[v] = True
    ans.append(v)
    for i in graph[v]:
        if not visited[i]:
            dfs(i)

graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
for _ in range(m):
    v1, v2 = map(int, input().rstrip().split())
    graph[v1].append(v2)
    graph[v2].append(v1)

dfs(1)
print(len(set(ans)) - 1)