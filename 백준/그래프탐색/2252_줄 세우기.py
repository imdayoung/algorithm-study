# 위상 정렬 알고리즘
import sys
from collections import deque


answer = []

N, M = map(int, sys.stdin.readline().split())
edges = [[] for _ in range(N + 1)]
ins = [0 for _ in range(N + 1)]

for _ in range(M):
    A, B = map(int, sys.stdin.readline().split())
    edges[A].append(B)
    ins[B] += 1

queue = deque()

for i in range(1, N + 1):
    if ins[i] == 0:
        queue.append(i)

while queue:
    node = queue.popleft()
    answer.append(node)
    
    for next_node in edges[node]:
        ins[next_node] -= 1
        if ins[next_node] == 0:
            queue.append(next_node)

print(*answer)
