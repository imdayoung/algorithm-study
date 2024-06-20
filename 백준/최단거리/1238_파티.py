import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        
        if distance[now] < dist:
            continue
        
        for i in graph[now]:
            cost = distance[now] + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


N, M, X = map(int, input().split())
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    Si, Ei, Ti = map(int, input().split())
    graph[Si].append((Ei, Ti))

answer = [0] * (N + 1)

distance = [INF] * (N + 1)
dijkstra(X)
for i in range(1, N + 1):
    answer[i] = distance[i]
    
for i in range(1, N + 1):
    distance = [INF] * (N + 1)
    dijkstra(i)
    answer[i] += distance[X]

print(max(answer))