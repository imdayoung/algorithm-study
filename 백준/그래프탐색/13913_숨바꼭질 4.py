from collections import deque

def bfs(x):
    queue = deque([[x, [x], 0]])
    visited[x] = True

    if N > K:
        return N - K, [x for x in range(N, K - 1, -1)]

    while queue:
        x, r, cnt = queue.popleft()
        if x == K:
            return cnt, r
        
        for nx in [x - 1, x + 1, x * 2]:
            if nx < 0 or nx > 100000:
                continue
            if not visited[nx]:
                visited[nx] = True
                route = r + [nx]
                queue.append([nx, route, cnt + 1])


N, K = map(int, input().split())
visited = [False] * 100001

cnt, route = bfs(N)
print(cnt)
print(*route)