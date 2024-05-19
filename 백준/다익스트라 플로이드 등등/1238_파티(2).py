import sys
import heapq


def dijkstra(start):
    distance = [INF for _ in range(N + 1)]
    distance[start] = 0
    q = []
    heapq.heappush(q, (0, start))

    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = distance[now] + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

    return distance


INF = int(1e9)

N, M, X = map(int, sys.stdin.readline().split())
answer = [0 for _ in range(N + 1)]

graph = [[] for _ in range(N + 1)]
for _ in range(M):
    start, end, time = map(int, sys.stdin.readline().split())
    graph[start].append((end, time))

# X로 가는 거리
for i in range(1, N + 1):
    dist_to_x = dijkstra(i)
    answer[i] = dist_to_x[X]

# X에서 가는 거리
dist_from_x = dijkstra(X)
for i in range(1, N + 1):
    answer[i] += dist_from_x[i]

print(max(answer))


# # 시간 초과
# import sys


# INF = int(1e9)
# answer = 0

# N, M, X = map(int, sys.stdin.readline().split())

# dist = [[INF for _ in range(N + 1)] for _ in range(N + 1)]
# for _ in range(M):
#     start, end, time = map(int, sys.stdin.readline().split())
#     dist[start][end] = time

# for i in range(1, N + 1):
#     for j in range(1, N + 1):
#         for k in range(1, N + 1):
#             dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

# for i in range(1, N + 1):
#     answer = max(answer, dist[i][X] + dist[X][i])

# print(answer)