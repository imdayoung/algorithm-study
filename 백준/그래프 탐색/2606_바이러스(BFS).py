from collections import deque
import sys
input = sys.stdin.readline

def bfs(v):
    queue = deque()
    queue.append(v)
    while queue:
        v = queue.popleft()
        res.append(v)
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

res = []
start = 1

N = int(input())
M = int(input())
visited = [False] * (N + 1)
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited[start] = True
bfs(start)
print(len(res) - 1)