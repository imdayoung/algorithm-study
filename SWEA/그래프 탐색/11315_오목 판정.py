def check():
    for x in range(N):
        for y in range(N):
            for i in range(4):
                if graph[x][y] == "o":
                    cnt = 1
                    nx = x + dx[i]
                    ny = y + dy[i]
                    while -1 < nx < N and -1 < ny < N and graph[nx][ny] == "o":
                        cnt += 1
                        if cnt >= 5:
                            return "YES"
                        nx += dx[i]
                        ny += dy[i]
    return "NO"

dx = [0, 1, 1, 1]
dy = [1, 0, 1, -1]

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    graph = [list(map(str, input())) for _ in range(N)]
    print(f"#{tc} {check()}")