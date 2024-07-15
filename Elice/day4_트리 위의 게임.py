import sys
from collections import deque


def make_tree():
    tree = [[] for _ in range(N + 1)]

    visited = [False for _ in range(N + 1)]
    visited[1] = True

    queue = deque(graph[1])

    for node in graph[1]:
        tree[1].append(node)
        visited[node] = True

    while queue:
        node = queue.popleft()
        for next_node in graph[node]:
            if not visited[next_node]:
                tree[node].append(next_node)
                queue.append(next_node)
                visited[next_node] = True

    return tree


def get_result(start):
    first, second = 0, 0

    turn = 0
    cur_node = start

    while tree[cur_node]:
        if turn == 0:
            first += cur_node
        else:
            second += cur_node

        cur_node = get_next_node(cur_node)
        turn = (turn + 1) % 2

    return first, second


def get_next_node(cur):
    node = cur
    return node


answers = []

N = int(sys.stdin.readline())
graph = [[] for _ in range(N + 1)]

for _ in range(N - 1):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

tree = make_tree()
print(tree)

for i in range(1, N + 1):
    cur = i
    first, second = get_result(cur)
    if first >= second:
        answers.append(1)
    else:
        answers.append(0)

for answer in answers:
    print(answer)
