from collections import deque


def bfs(x, n, c):
    queue = deque([x])
    visited[x] = True
    while queue:
        x = queue.popleft()
        
        for i in range(len(c[x])):
            if not visited[i] and c[x][i] == 1:
                visited[i] = True
                queue.append(i)


def solution(n, computers):
    answer = 0
    global visited
    visited = [False for _ in range(n)]
    
    for c in computers:
        print(c)

    for i in range(n):
        if not visited[i]:
            answer += 1
            bfs(i, n, computers)

    return answer


visited = []