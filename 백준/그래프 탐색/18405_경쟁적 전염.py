from collections import deque
import sys


def bfs(virus_num, start):    
    queue = deque(start)
    new_viruses = []

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx > N - 1 or ny < 0 or ny > N - 1:
                continue

            if board[nx][ny] == 0:
                board[nx][ny] = virus_num
                new_viruses.append((nx, ny))

    viruses[virus_num] = new_viruses


dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

# N X N 크기의 시험관, 1번부터 K번까지의 바이러스 종류
N, K = map(int, sys.stdin.readline().split())
board = []
viruses = [[] for _ in range(K + 1)]
for i in range(N):
    row = list(map(int, sys.stdin.readline().split()))
    board.append(row)
    for j in range(N):
        if row[j] == 0:
            continue
        viruses[row[j]].append((i, j))

# S초 후 X, Y에 존재하는 바이러스의 종류
S, X, Y = map(int, sys.stdin.readline().split())
for _ in range(S):
    for i in range(1, K + 1):
        bfs(i, viruses[i])

print(board[X - 1][Y - 1])