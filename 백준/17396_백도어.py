import sys
import heapq


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        
        for i in times[now]:
            cost = distance[now] + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


INF = int(1e20)

N, M = map(int, sys.stdin.readline().split())
is_visible = list(map(int, sys.stdin.readline().split()))
is_visible[N - 1] = 0

times = [[] for _ in range(N)]

for _ in range(M):
    a, b, t = map(int, sys.stdin.readline().split())
    if is_visible[a] or is_visible[b]:
        continue
    times[a].append((b, t))
    times[b].append((a, t))

distance = [INF for _ in range(N)]
dijkstra(0)

if distance[N - 1] == INF:
    answer = -1
else:
    answer = distance[N - 1]
    
print(answer)