import sys
from collections import deque


def bfs(x, target):
    queue = deque([x])
    visited = [-1 for _ in range(100000 + 1)]
    visited[x] = 0
    
    while queue:
        x = queue.popleft()
        if x == target:
            return visited[x]
        
        for nx in [x - 1, x + 1, x * 2]:
            if nx < 0 or nx > 100000:
                continue
            if visited[nx] == -1:
                visited[nx] = visited[x] + 1
                queue.append(nx)
                
    return -1
        

N, K = map(int, sys.stdin.readline().split())
print(bfs(N, K))