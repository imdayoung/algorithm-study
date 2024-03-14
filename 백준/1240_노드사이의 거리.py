import sys


def dfs(node, d, target):
    global answer
    visited[node] = True
    if node == target:
        answer = d
        return
    
    for next_node, distance in tree[node]:
        if not visited[next_node]:
            dfs(next_node, d + distance, target)


N, M = map(int, sys.stdin.readline().split())
tree = [[] for _ in range(N + 1)]

for _ in range(N - 1):
    a, b, d = map(int, sys.stdin.readline().split())
    tree[a].append((b, d))
    tree[b].append((a, d))

for _ in range(M):
    answer = 0
    visited = [False for _ in range(N + 1)]
    a, b = map(int, sys.stdin.readline().split())
    dfs(a, 0, b)
    print(answer)


# # 플로이드 -> 시간 초과
# import sys


# INF = int(1e9)

# N, M = map(int, sys.stdin.readline().split())
# graph = [[INF for _ in range(N + 1)] for _ in range(N + 1)]
# for i in range(1, N + 1):
#     graph[i][i] = 0

# for _ in range(N - 1):
#     a, b, c = map(int, sys.stdin.readline().split())
#     graph[a][b] = min(graph[a][b], c)
#     graph[b][a] = min(graph[b][a], c)

# for i in range(1, N + 1):
#     for j in range(1, N + 1):
#         for k in range(1, N + 1):
#             graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

# for _ in range(M):
#     a, b = map(int, sys.stdin.readline().split())
#     print(graph[a][b])