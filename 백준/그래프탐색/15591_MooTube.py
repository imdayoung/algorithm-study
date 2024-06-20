from collections import deque
import sys
input = sys.stdin.readline


def usado(v):
    result = 0
    queue = deque([v])
    visited[v] = True
    while queue:
        v = queue.popleft()
        for nv, dist in graph[v]:
            if not visited[nv] and dist >= k:
                queue.append(nv)
                visited[nv] = True
                result += 1
    return result


N, Q = map(int, input().split())
graph = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    p, q, r = map(int, input().split())
    graph[p].append((q, r))
    graph[q].append((p, r))

for _ in range(Q):
    k, v = map(int, input().split())
    visited = [False] * (N + 1)
    print(usado(v))