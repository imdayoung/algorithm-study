from collections import deque
import sys
input = sys.stdin.readline

def bfs(x):
    queue = deque([x])

    while queue:
        x = queue.popleft()
        if x == 100:
            return visited[x]
        
        for i in range(1, 7):
            dx = x + i
            if dx > 100:
                continue
            if dx in objs:
                dx = objs[dx]
            if visited[dx] == 0:
                visited[dx] = visited[x] + 1
                queue.append(dx)

objs = {}
visited = [0 for _ in range(101)]
# 사다리의 수 n, 뱀의 수 m
n, m = map(int, input().split())
for _ in range(n + m):
    start, end = map(int, input().split())
    objs[start] = end

print(bfs(1))