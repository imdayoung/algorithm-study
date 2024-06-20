from collections import deque
import sys


def bfs(now):
    queue = deque([now])
    visited[now] = 0
    while queue:
        now = queue.popleft()
        if now == G:
            return visited[now]
        for next_stair in [now + U, now - D]:
            if next_stair > F or next_stair < 1:
                continue
            if not visited[next_stair] and next_stair != now:
                visited[next_stair] = visited[now] + 1
                queue.append(next_stair)
    return "use the stairs"


F, S, G, U, D = map(int, sys.stdin.readline().split())
visited = [False] * (F + 1)
print(bfs(S))