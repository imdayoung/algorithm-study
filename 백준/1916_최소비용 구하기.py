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
        
        for i in graph[cur]:
            cost = distance[cur] + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(queue, (i[0], cost))
    
    return distance[end]


INF = int(1e9)

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

graph = [[] for _ in range(N + 1)]
for _ in range(M):
    start, end, cost = map(int, sys.stdin.readline().split())
    graph[start].append((end, cost))
    
current, destination = map(int, sys.stdin.readline().split())
print(dijkstra(current, destination))