import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

def dfs(x, y):
    global cnt
    if x <= -1 or y <= -1 or x >= n or y >= n:
        return False
    if graph[x][y] == 1:
        graph[x][y] = 0
        cnt += 1
        dfs(x - 1, y)
        dfs(x + 1, y)
        dfs(x, y - 1)
        dfs(x, y + 1)
        return True
    return False

n = int(input().rstrip())
graph = []
result1 = 0
result2 = []
for _ in range(n):
    graph.append(list(map(int, input().rstrip())))

for i in range(n):
    for j in range(n):
        cnt = 0
        if dfs(i, j):
            result1 += 1
            result2.append(cnt)

print(result1)
result2.sort()
for i in result2:
    print(i)