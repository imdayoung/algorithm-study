import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

def dfs(x, y, rain):
    if x < 0 or x > N - 1 or y < 0 or y > N - 1:
        return False
    if ground[x][y] > rain and not visited[x][y]:
        visited[x][y] = True
        dfs(x + 1, y, rain)
        dfs(x - 1, y, rain)
        dfs(x, y + 1, rain)
        dfs(x, y - 1, rain)
        return True
    return False


answer = 1

N = int(input())
ground = []
min_value = 100
max_value = 1

for _ in range(N):
    temp = list(map(int, input().split()))
    for i in range(N):
        if temp[i] < min_value:
            min_value = temp[i]
        elif temp[i] > max_value:
            max_value = temp[i]
    ground.append(temp)

for k in range(min_value, max_value):
    cnt = 0
    visited = [[False] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if ground[i][j] > k and not visited[i][j]:
                dfs(i, j, k)
                cnt += 1
    if cnt >= answer:
        answer = cnt
    
print(answer)