import sys
import heapq


def dijkstra(start, end):
    distance = [INF for _ in range(N + 1)]
    distance[start] = 0
    
    queue = []
    heapq.heappush(queue, (start, 0))
    while queue:
        cur, dist = heapq.heappop(queue)
        if distance[cur] < dist:
            continue
        
        for to, cost in graph[cur]:
            cost = dist + cost
            if cost < distance[to]:
                distance[to] = cost
                heapq.heappush(queue, (to, cost))

    return distance[end]


INF = int(1e9)

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

graph = [[] for _ in range(N + 1)]
for _ in range(M):
    start, end, cost = map(int, sys.stdin.readline().split())
    graph[start].append((end, cost))

start, end = map(int, sys.stdin.readline().split())

print(dijkstra(start, end))