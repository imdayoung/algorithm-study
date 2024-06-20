from collections import deque
import sys
input = sys.stdin.readline

def bfs(v):
    queue = deque([(v)])
    visited = [0] * 100001
    while queue:
        v = queue.popleft()
        if v == M:
            return visited[M]    
        
        for nv in [v + 1, v - 1, v + A, v - A, v + B, v - B, v * A, v * B]:
            if nv < 0 or nv > 100000:
                continue
            if not visited[nv]:
                visited[nv] = visited[v] + 1
                queue.append(nv)    
    return -1
               

A, B, N, M = map(int, input().split())
print(bfs(N))