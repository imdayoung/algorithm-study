import heapq


INF = int(1e9)

def dijkstra(N, edges, K, start):
    result = 0
    
    distances = [INF for _ in range(N + 1)]
    distances[start] = 0
    
    q = []
    heapq.heappush(q, (start, 0))
    
    while q:
        cur, dist = heapq.heappop(q)
        if distances[cur] < dist:
            continue
            
        for to, cost in edges[cur]:
            cost += distances[cur]
            if cost < distances[to]:
                distances[to] = cost
                heapq.heappush(q, (to, cost))
            
    for distance in distances:
        if distance <= K:
            result += 1
            
    return result


def solution(N, road, K):    
    edges = [[] for _ in range(N + 1)]
    for a, b, c in road:
        edges[a].append((b, c))
        edges[b].append((a, c))

    return dijkstra(N, edges, K, 1)