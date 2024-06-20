from collections import deque

def bfs(x):
    queue = deque([x])

    while queue:
        x = queue.popleft()
        if x == K:
            return

        for nx in [x - 1, x + 1, x * 2]:
            if nx < 0 or nx > 100000:
                continue
            if not visited[nx]:
                visited[nx] = visited[x] + 1
                queue.append(nx)


N, K = map(int, input().split())
visited = [0] * 100001
bfs(N)
print(visited[K])