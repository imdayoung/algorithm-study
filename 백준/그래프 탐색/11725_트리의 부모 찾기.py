import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)


def make_tree(x):
    visited[x] = True
    for i in graph[x]:
        if not visited[i]:
            parent_node[i] = x
            make_tree(i)
            tree[x].append(i)


N = int(input())
graph = [[0] for _ in range(N + 1)]
visited = [False] * (N + 1)
parent_node = [0] * (N + 1)

for _ in range(N - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

tree = [[0] for _ in range(N + 1)]
make_tree(1)

for i in range(2, N + 1):
    print(parent_node[i])