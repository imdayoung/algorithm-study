import sys
from collections import deque


def bfs(start, num):
    queue = deque([start])
    visited = [-1 for _ in range(num + 1)]
    visited[start] = 0

    while queue:
        num = queue.popleft()
        for next_num in friends[num]:
            if visited[next_num] == -1:
                visited[next_num] = visited[num] + 1
                queue.append(next_num)

    return max(visited)


num = int(sys.stdin.readline())
friends = [[] for _ in range(num + 1)]

while True:
    friend1, friend2 = map(int, sys.stdin.readline().split())
    if friend1 == -1 and friend2 == -1:
        break

    friends[friend1].append(friend2)
    friends[friend2].append(friend1)

score = int(1e9)
candidates = []
for i in range(1, num + 1):
    dist = bfs(i, num)
    if dist < score:
        score = dist
        candidates = [i]
    elif dist == score:
        candidates.append(i)

print(score, len(candidates))
print(*candidates)