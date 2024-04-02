import sys


def transform(x, y):
    for i in range(x, x + 3):
        for j in range(y, y + 3):
            matrix[i][j] = (matrix[i][j] + 1) % 2


answer = 0

N, M = map(int, sys.stdin.readline().split())
matrix = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(N)]
target = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(N)]

for i in range(N - 2):
    for j in range(M - 2):
        if matrix[i][j] != target[i][j] and i + 2 < N and j + 2 < M:
            transform(i, j)
            answer += 1

for i in range(N):
    for j in range(M):
        if matrix[i][j] != target[i][j]:
            answer = -1

print(answer)