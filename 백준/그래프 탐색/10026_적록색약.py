import copy
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

def dfs_rg(x, y):
    if x <= -1 or y <= -1 or x >= n or y >= n:
        return False
    if graph_colored[x][y] == "R" or graph_colored[x][y] == "G":
        graph_colored[x][y] = "A"
        dfs_rg(x - 1, y)
        dfs_rg(x + 1, y)
        dfs_rg(x, y - 1)
        dfs_rg(x, y + 1)
        return True
    return False

def dfs_r(x, y):
    if x <= -1 or y <= -1 or x >= n or y >= n:
        return False
    if graph[x][y] == "R":
        graph[x][y] = "A"
        dfs_r(x - 1, y)
        dfs_r(x + 1, y)
        dfs_r(x, y - 1)
        dfs_r(x, y + 1)
        return True
    return False

def dfs_g(x, y):
    if x <= -1 or y <= -1 or x >= n or y >= n:
        return False
    if graph[x][y] == "G":
        graph[x][y] = "A"
        dfs_g(x - 1, y)
        dfs_g(x + 1, y)
        dfs_g(x, y - 1)
        dfs_g(x, y + 1)
        return True
    return False

def dfs_b(x, y):
    if x <= -1 or y <= -1 or x >= n or y >= n:
        return False
    if graph_colored[x][y] == "B":
        graph_colored[x][y] = "A"
        dfs_b(x - 1, y)
        dfs_b(x + 1, y)
        dfs_b(x, y - 1)
        dfs_b(x, y + 1)
        return True
    return False

n = int(input().rstrip())
graph = []
graph_colored = []
result_rg, result_r, result_g, result_b = 0, 0, 0, 0

for _ in range(n):
    temp = list(input().rstrip())
    graph.append(temp)
graph_colored = copy.deepcopy(graph)

for i in range(n):
    for j in range(n):
        if dfs_b(i, j):
            result_b += 1
        if dfs_rg(i, j):
            result_rg += 1
        if dfs_r(i, j):
            result_r += 1
        if dfs_g(i, j):
            result_g += 1
        
print(result_r + result_g + result_b, result_rg + result_b)