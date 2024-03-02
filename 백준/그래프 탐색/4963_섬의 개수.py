import sys
sys.setrecursionlimit(10000)

def dfs(x, y, graph):
    if x <= -1 or x >= h or y <= -1 or y >= w:
        return False
    if graph[x][y] == 1:
        graph[x][y] = 0
        dfs(x - 1, y - 1, graph)
        dfs(x - 1, y, graph)
        dfs(x - 1, y + 1, graph)
        dfs(x, y - 1, graph)
        dfs(x, y + 1, graph)
        dfs(x + 1, y - 1, graph)
        dfs(x + 1, y, graph)
        dfs(x + 1, y + 1, graph)
        return True
    return False

# 너비 w, 높이 h
w, h = map(int, input().split())

while w != 0 and h != 0:
    result = 0
    graph = []
    for _ in range(h):
        temp = list(map(int, input().rstrip().split()))
        graph.append(temp)
    # print(graph)
    for i in range(h):
        for j in range(w):
            if dfs(i, j, graph) == True:
                result += 1
    print(result)
    w, h = map(int, input().split())