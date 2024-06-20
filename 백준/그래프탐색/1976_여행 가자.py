import sys
from collections import deque


def bfs(start, target):
    queue = deque([start])
    visited = [False for _ in range(N + 1)]
    visited[start] = True

    while queue:
        city = queue.popleft()
        if city == target:
            return True
        for next_city in cities[city]:
            if not visited[next_city]:
                visited[next_city] = True
                queue.append(next_city)

    return False


answer = "YES"

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
cities = [[] for _ in range(N + 1)]
for start in range(N):
    infos = list(map(int, sys.stdin.readline().split()))
    for i in range(0, start):
        if infos[i] == 1:
            cities[start + 1].append(i + 1)
            cities[i + 1].append(start + 1)
plan = list(map(int, sys.stdin.readline().split()))

for i in range(M - 1):
    if not bfs(plan[i], plan[i + 1]):
        answer = "NO"
        break

print(answer)