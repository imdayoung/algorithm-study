def check(x, y, color):
    change = []
    for k in range(8):
        nx = x + dx[k]
        ny = y + dy[k]

        while True:
            if nx < 0 or nx > N - 1 or ny < 0 or ny > N - 1:
                change = []
                break
            if graph[nx][ny] == 0:
                change = []
                break
            if graph[nx][ny] == color:
                break
            else:
                change.append((nx, ny))
                nx += dx[k]
                ny += dy[k]
            
        for rx, ry in change:
            graph[rx][ry] = color

dx = [0, 0, 1, -1, 1, 1, -1, -1]
dy = [1, -1, 0, 0, 1, -1, 1, -1]

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    graph = [[0] * N for _ in range(N)]
    # 초기 흑돌과 백돌 배치 후 시작 (1 흑돌, 2 백돌)
    graph[N//2 - 1][N//2 - 1], graph[N//2][N//2] = 2, 2
    graph[N//2 - 1][N//2], graph[N//2][N//2 - 1] = 1, 1
    
    for _ in range(M):
        y, x, color = map(int, input().split())
        check(x - 1, y - 1, color)
        graph[x - 1][y - 1] = color

    count_1, count_2 = 0, 0
    for g in graph:
        count_1 += g.count(1)
        count_2 += g.count(2)
    print(f"#{tc} {count_1} {count_2}")