import sys
from collections import deque


def bfs(stores):
    global distance
    global answer

    queue = deque(stores)
    visited = [-1 for _ in range(N + 1)]
    visited[0], visited[stores[0]], visited[stores[1]] = 0, 0, 0

    while queue:
        building = queue.popleft()
        for next_building in roads[building]:
            if visited[next_building] == -1:
                visited[next_building] = visited[building] + 1
                queue.append(next_building)

    dist_sum = sum(visited)
    if dist_sum < distance:
        distance = dist_sum
        answer = [(stores[0], stores[1], dist_sum * 2)]


def backtracking(building, stores):
    if len(stores) == 2:
        bfs(stores)
        return
    
    for i in range(building + 1, N + 1):
        backtracking(i, stores + [i])


answer = []
distance = int(1e9)
N, M = map(int, sys.stdin.readline().split())

roads = [[] for _ in range(N + 1)]
for _ in range(M):
    A, B = map(int, sys.stdin.readline().split())
    roads[A].append(B)
    roads[B].append(A)

backtracking(0, [])
print(answer[0][0], answer[0][1], answer[0][2])