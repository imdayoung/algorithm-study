from collections import deque

def bfs(v):
    queue = deque([v])
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if i == 99:
                return 1
            queue.append(i)
            
    return 0

T = 10
for _ in range(T):
    tc, N = map(int, input().split())
    graph = [[] for _ in range(100)]
    routes = list(map(int, input().split()))

    for i in range(0, N * 2, 2):
        graph[routes[i]].append(routes[i + 1])

    print(f"#{tc} {bfs(0)}")