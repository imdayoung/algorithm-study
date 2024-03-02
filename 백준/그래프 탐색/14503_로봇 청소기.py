import sys
input = sys.stdin.readline

def check_empty(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx > N - 1 or ny < 0 or ny > M - 1:
            continue
        if room[nx][ny] == 0:
            return 1
    return 0


cnt = 0

N, M = map(int, input().split())
r, c, d = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(N)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

while True:
    if room[r][c] == 0:
        room[r][c] = 2
        cnt += 1

    # 주변 4칸 중 청소되지 않은 빈 칸이 있는 경우
    if check_empty(r, c):
        for _ in range(4):
            d = (d + 3) % 4
            if room[r + dx[d]][c + dy[d]] == 0:
                r += dx[d]
                c += dy[d]
                break

    # 주변 4칸 중 청소되지 않은 빈 칸이 없는 경우
    else:
        r -= dx[d]
        c -= dy[d]
        if r < 0 or r > N - 1 or c < 0 or c > M - 1 or room[r][c] == 1:
            break

print(cnt)