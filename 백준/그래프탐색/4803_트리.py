import sys


def dfs(from_node, to_node):
    global cycle_flag

    visited[to_node] = True

    for next_node in graph[to_node]:
        if next_node == from_node:
            continue

        if visited[next_node]:
            cycle_flag = 1
            return

        if not visited[next_node]:
            dfs(to_node, next_node)
            

case_num = 0
while True:
    case_num += 1

    n, m = map(int, sys.stdin.readline().split())
    if n == 0 and m == 0:
        break

    graph = [[] for _ in range(n + 1)]
    visited = [False for _ in range(n + 1)]
    for _ in range(m):
        a, b = map(int, sys.stdin.readline().split())
        graph[a].append(b)
        graph[b].append(a)

    tree = 0
    for i in range(1, n + 1):
        cycle_flag = 0
        if not visited[i]:
            dfs(i, i)
            if cycle_flag == 0:
                tree += 1

    if tree == 0:
        print(f'Case {case_num}: No trees.')
    elif tree == 1:
        print(f'Case {case_num}: There is one tree.')
    else:
        print(f'Case {case_num}: A forest of {tree} trees.')