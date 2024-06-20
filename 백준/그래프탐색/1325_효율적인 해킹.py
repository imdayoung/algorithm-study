from collections import deque
import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

def bfs(v):
    cnt = 0
    visited = [False for _ in range(N + 1)]
    queue = deque([v])
    visited[v] = True
    while queue:
        v = queue.popleft()
        cnt += 1
        for x in graph[v]:
            if not visited[x]:
                queue.append(x)
                visited[x] = True
    return cnt
            
N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
answer = []

for _ in range(M):
    A, B = map(int, input().split())
    graph[B].append(A)

for i in range(1, N + 1):
    answer.append(bfs(i))

max_computer = max(answer)
for i in range(len(answer)):
    if answer[i] == max_computer:
        print(i + 1, end = " ")