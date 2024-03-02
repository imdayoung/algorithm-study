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

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
parent = [i for i in range(N + 1)]
edges = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]
edges.sort(key = lambda x:x[2])

for i in range(M):
    if find(parent[edges[i][0]]) != find(parent[edges[i][1]]):
        answer += edges[i][2]
        union(edges[i][0], edges[i][1])

print(answer)