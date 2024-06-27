# 최소 스패팅 트리, Kruskal Algorithm, Union-Find
import sys


def find(a):
    if parent[a] == a:
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

max_cost = 0

parent = [i for i in range(N + 1)]

for start, end, cost in edges:
    if find(start) == find(end):
        continue
    
    answer += cost
    union(start, end)
    max_cost = max(max_cost, cost)
    
print(answer - max_cost)