import sys


def bfs():
    

R, C = map(int, sys.stdin.readline().split())
yard = [list(map(str, sys.stdin.readline().rstrip())) for _ in range(R)]
print(yard)

for i in range(R):
    for j in range(C):
        if yard[i][j] == 'o':
            bfs(i, j)