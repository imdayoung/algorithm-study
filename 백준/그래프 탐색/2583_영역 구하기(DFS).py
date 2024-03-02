import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

def dfs(x, y):
    global size
    if x < 0 or x > N - 1 or y < 0 or y > M - 1:
        return False
    if board[x][y] == 1:
        board[x][y] = 0
        size += 1
        dfs(x + 1, y)
        dfs(x - 1, y)
        dfs(x, y + 1)
        dfs(x, y - 1)
        return True
    return False


M, N, K = map(int, input().split())
board = [[1] * M for _ in range(N)]
visited = [[False] * M for _ in range(N)]
for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(x1, x2):
        for j in range(y1, y2):
            board[i][j] = 0

sizes = []
cnt = 0
for i in range(N):
    for j in range(M):
        size = 0
        if board[i][j] == 1:
            cnt += 1
            dfs(i, j)
            sizes.append(size)

sizes.sort()
print(cnt)
print(*sizes)