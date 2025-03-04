import heapq


INF = int(1e9)

def dijkstra(start, n, edges):
    distances = [INF for _ in range(n + 1)]
    distances[start] = 0
    
    q = []
    heapq.heappush(q, (start, 0))
    
    while q:
        cur, dist = heapq.heappop(q)
        if distances[cur] < dist:
            continue
            
        for to, cost in edges[cur]:
            cost += dist
            if cost < distances[to]:
                distances[to] = cost
                heapq.heappush(q, (to, cost))

    return distances


def solution(n, s, a, b, fares):    
    edges = [[] for _ in range(n + 1)]
    for node1, node2, cost in fares:
        edges[node1].append((node2, cost))
        edges[node2].append((node1, cost))
        
    distances_from_s = dijkstra(s, n, edges)
    distances_to_a = dijkstra(a, n, edges)
    distances_to_b = dijkstra(b, n, edges)
    
    answer = distances_from_s[a] + distances_from_s[b]

    for i in range(n + 1):
        temp = distances_from_s[i] + distances_to_a[i] + distances_to_b[i]
        answer = min(answer, temp)
        
    return answer