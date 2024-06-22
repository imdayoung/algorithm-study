# 최소 스패팅 트리, Kruskal Algorithm, Union-Find
import sys


def find(a):
    if a == parent[a]:
        return a
    return find(parent[a])
    
    
def union(a, b):
    a = find(a)
    b = find(b)
    
    if a < b:
        parent[b] = a
    else:
        parent[a] = b
    
    
answer = 0

N, M = map(int, sys.stdin.readline().split())
edges = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]
edges.sort(key = lambda x : x[2])
max_edge = 0

parent = [i for i in range(N + 1)]
for i in range(M):
    if find(edges[i][0]) != find(edges[i][1]):
        answer += edges[i][2]
        max_edge = max(max_edge, edges[i][2])
        union(edges[i][0], edges[i][1])

print(answer - max_edge)