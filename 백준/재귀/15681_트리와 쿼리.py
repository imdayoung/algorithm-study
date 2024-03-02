import sys
sys.setrecursionlimit(10 ** 8)


def count_sub_tree(node):
    count[node] = 1
    for child in tree[node]:
        if count[child] == 0:
            count_sub_tree(child)
            count[node] += count[child]


answers = []
N, R, Q = map(int, sys.stdin.readline().split())
tree = [[] for _ in range(N + 1)]
count = [0] * (N + 1)

for _ in range(N - 1):
    U, V = map(int, sys.stdin.readline().split())
    tree[U].append(V)
    tree[V].append(U)

count_sub_tree(R)

for _ in range(Q):
    U = int(sys.stdin.readline())
    answers.append(count[U])

for answer in answers:
    print(answer)


# # 시간 초과
# from collections import deque
# import sys


# def graph_to_tree(node):
#     tree = [[] for _ in range(N + 1)]

#     queue = deque([node])
#     visited = [False] * (N + 1)
#     visited[node] = True

#     while queue:
#         parent = queue.popleft()
#         for child in graph[parent]:
#             if not visited[child]:
#                 visited[child] = True
#                 tree[parent].append(child)
#                 queue.append(child)

#     return tree


# def dfs(node):
#     global cnt
#     visited[node] = True
#     for node in tree[node]:
#         if not visited[node]:
#             cnt += 1
#             dfs(node)


# answers = []
# N, R, Q = map(int, sys.stdin.readline().split())
# graph = [[] for _ in range(N + 1)]

# for _ in range(N - 1):
#     U, V = map(int, sys.stdin.readline().split())
#     graph[U].append(V)
#     graph[V].append(U)

# tree = graph_to_tree(R)

# for _ in range(Q):
#     U = int(sys.stdin.readline())
#     cnt = 1
#     visited = [False] * (N + 1)
#     dfs(U)
#     answers.append(cnt)

# for answer in answers:
#     print(answer)
