from collections import deque
import sys
input = sys.stdin.readline


def bfs(n):
    kevin_num = 0
    queue = deque([n])
    visited[n] = 0
    while queue:
        n = queue.popleft()
        for friend in graph[n]:
            if visited[friend] == -1:
                visited[friend] = visited[n] + 1
                kevin_num += visited[friend]
                queue.append(friend)
    return kevin_num


N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    A, B = map(int, input().split())
    if B not in graph[A]:
        graph[A].append(B)
        graph[B].append(A)

answer = 0
min_val = int(1e9)
for i in range(1, N + 1):
    visited = [-1] * (N + 1)
    kevin_num = bfs(i)
    if kevin_num < min_val:
        min_val = kevin_num
        answer = i

print(answer)