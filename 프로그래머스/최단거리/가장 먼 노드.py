import heapq


INF = int(1e9)

def dijkstra(n, edges, start):
    result = 0
    
    distances = [INF for _ in range(n + 1)]
    distances[start] = 0
    q = []
    heapq.heappush(q, (start, 0))
    
    while q:
        cur, dist = heapq.heappop(q)
        if distances[cur] < dist:
            continue
            
        for to in edges[cur]:
            cost = dist + 1
            if cost < distances[to]:
                heapq.heappush(q, (to, cost))
                distances[to] = cost

    MAX_VALUE = 0
    for distance in distances:
        if distance != INF and distance > MAX_VALUE:
            MAX_VALUE = distance
    
    for distance in distances:
        if distance == MAX_VALUE:
            result += 1
            
    return result
    
    
def solution(n, edge):
    edges = [[] for _ in range(n + 1)]
    for e in edge:
        edges[e[0]].append(e[1])
        edges[e[1]].append(e[0])    
    
    return dijkstra(n, edges, 1)