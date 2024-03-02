from collections import deque
import sys
input = sys.stdin.readline

def dfs(v):
    visited[v] = True
    print(v, end = ' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(i)

def bfs(v):
    queue = deque([v])
    visited[v] = True
    while queue:
        v = queue.popleft()
        print(v, end = ' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

# N 정점의 개수, M 간선의 개수, V 탐색을 시작할 정점의 번호
n, m, v = map(int, input().rstrip().split())

graph = [[] for _ in range(n + 1)]
# 그래프 생성
for _ in range(m):
    v1, v2 = map(int, input().rstrip().split())
    graph[v1].append(v2)
    graph[v2].append(v1)
# 그래프 오름차순 정렬
for i in graph:
    i.sort()

visited = [False] * (n + 1)
dfs(v)
print()
visited = [False] * (n + 1)
bfs(v)