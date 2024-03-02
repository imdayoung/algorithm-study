# Kruskal Algorithm
import sys

# 루트 노드를 찾는 함수
def find(a):
    # 자기 자신이 루트 노드이면 반환
    if a == parent[a]:
        return a
    # a의 루트 노드 반환
    return find(parent[a])


# a가 속해있는 트리와 b가 속해있는 트리를 합치는 연산
def union(a, b):
    # a, b의 루트 노드 찾기
    a = find(a)
    b = find(b)

    # 값이 더 작은 쪽이 부모 노드
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


answer = 0

V, E = map(int, sys.stdin.readline().split())
edges = [list(map(int, sys.stdin.readline().split())) for _ in range(E)]
edges.sort(key = lambda x : x[2])

parent = [i for i in range(V + 1)]
for i in range(E):
    if find(edges[i][0]) != find(edges[i][1]):
        answer += edges[i][2]
        union(edges[i][0], edges[i][1])

print(answer)