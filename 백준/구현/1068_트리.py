from collections import deque


N = int(input())
tree = [[] for _ in range(N)]

parents = list(map(int, input().split()))
for i in range(N):
    if parents[i] != -1:
        tree[parents[i]].append(i)
    if parents[i] == -1:
        root = i

del_node = int(input())

if del_node == root:
    print(0)
    exit()

queue = deque([del_node])
while queue:
    node = queue.popleft()
    for next_node in tree[node]:
        tree[next_node] = []
        queue.append(next_node)
    tree[node] = []

answer = 0
queue = deque([root])
while queue:
    node = queue.popleft()
    if tree[node] == [] or tree[node] == [del_node]:
        answer += 1
    for next_node in tree[node]:
        if next_node == del_node:
            continue
        queue.append(next_node)

print(answer)