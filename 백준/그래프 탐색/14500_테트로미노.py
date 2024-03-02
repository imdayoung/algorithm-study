import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)


# ㅗ, ㅜ, ㅏ, ㅓ 모양 제외
def dfs(x, y, cnt, sum_num):
    global answer
    if cnt == 4:
        answer = max(answer, sum_num)
        return
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx > N - 1 or ny < 0 or ny > M - 1:
            continue
        if not visited[nx][ny]:
            visited[x][y] = True
            dfs(nx, ny, cnt + 1, sum_num + board[nx][ny])
            visited[x][y] = False


# ㅗ, ㅜ, ㅏ ㅓ 모양 탐색
def vowel(x, y):
    global answer
    for i in range(4):
        temp = board[x][y]
        for j in range(3):
            k = (i + j) % 4
            nx = x + dx[k]
            ny = y + dy[k]
            if nx < 0 or nx > N - 1 or ny < 0 or ny > M - 1:
                break
            temp += board[nx][ny]
        answer = max(answer, temp)
    

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

answer = 0
visited = [[False] * M for _ in range(N)]
for i in range(N):
    for j in range(M):
        visited[i][j] = True
        dfs(i, j, 1, board[i][j])
        visited[i][j] = False
        vowel(i, j)

print(answer)