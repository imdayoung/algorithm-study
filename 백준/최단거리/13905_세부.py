import sys
import heapq


def dijkstra(start, end):
    distance = [0 for _ in range(N + 1)]
    distance[start] = 0
    
    q = []
    heapq.heappush(q, (start, -INF))
    
    while q:
        cur, dist = heapq.heappop(q)
        dist = -dist
        
        if distance[cur] > dist:
            continue
        
        for to, cost in edges[cur]:
            cost = min(cost, dist)
            if cost > distance[to]:
                distance[to] = cost
                heapq.heappush(q, (to, -cost))
    
    return distance[end]


INF = int(1e9)

N, M = map(int, sys.stdin.readline().split())
s, e = map(int, sys.stdin.readline().split())
edges = [[] for _ in range(N + 1)]

for _ in range(M):
    h1, h2, k = map(int, sys.stdin.readline().split())
    edges[h1].append((h2, k))
    edges[h2].append((h1, k))

print(dijkstra(s, e))
