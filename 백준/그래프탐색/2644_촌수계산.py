import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

def dfs(v, num):
    num += 1
    visited[v] = True
    if v == b:
        result.append(num)
    for i in graph[v]:
        if not visited[i]:
            dfs(i, num)

# 전체 사람의 수 n
n = int(input().rstrip())
graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
result = []
# 촌수를 계산해야 하는 서로 다른 두 사람의 번호
a, b = map(int, input().rstrip().split())
# 부모 자식들 간의 관계의 개수 m
m = int(input().rstrip())
# 넷째 줄부터는 부모 자식간의 관계를 나타내는 두 번호 x,y가 각 줄에 나온다.
for _ in range(m):
    x, y = map(int, input().rstrip().split())
    graph[x].append(y)
    graph[y].append(x)

dfs(a, 0)
if result:
    print(result[0] - 1)
else:
    print(-1)