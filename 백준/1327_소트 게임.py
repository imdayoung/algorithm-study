import sys
from collections import deque


def bfs(start):
    queue = deque([start])
    visited[start] = 0

    while queue:
        now = queue.popleft()
        if now == target:
            return visited[now]
        
        for i in range(0, N - K + 1):
            temp = now[:i] + now[i:i + K][::-1] + now[i + K:]
            if temp not in visited:
                queue.append(temp)
                visited[temp] = visited[now] + 1

    return -1


N, K = map(int, sys.stdin.readline().split())
target = ''.join(str(i) for i in range(1, N + 1))

nums = ''.join(str(i) for i in list(map(int, sys.stdin.readline().split())))
visited = {}

print(bfs(nums))