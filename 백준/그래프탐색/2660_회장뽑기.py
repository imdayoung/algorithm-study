from collections import deque
import sys
input = sys.stdin.readline


def bfs(x, cnt):
    queue = deque([(x, cnt)])
    visited = [False] * (N + 1)
    visited[x] = True

    while queue:
        x, cnt = queue.popleft()
        for nx in relation[x]:
            if not visited[nx]:
                visited[nx] = True
                queue.append((nx, cnt + 1))

    return cnt


N = int(input())
relation = [[] for _ in range(N + 1)]

x, y = map(int, input().split())
while x != -1 and y != -1:
    relation[x].append(y)
    relation[y].append(x)
    x, y = map(int, input().split())

min_value = N
answers = []

for i in range(1, N + 1):
    cnt = bfs(i, 0)
    if cnt < min_value:
        min_value = cnt
        answers = [i]
    elif cnt == min_value:
        answers.append(i)

print(min_value, len(answers))
print(*answers)