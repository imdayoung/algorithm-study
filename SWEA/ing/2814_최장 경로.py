import sys
sys.stdin = open("input.txt", "r")
INF = int(1e9)

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    # 간선이 없는 경우 최장 경로 1 출력
    if M == 0:
        print(f'#{tc} 1')
        continue

    graph = [[INF] * (N + 1) for _ in range(N + 1)]
    
    for _ in range(M):
        x, y = map(int, input().split())
        graph[x][y] = 1
        graph[y][x] = 1

    for x in range(N + 1):
        for y in range(N + 1):
            if x == y:
                graph[x][y] = 0

    for k in range(1, N + 1):
        for x in range(1, N + 1):
            for y in range(1, N + 1):
                graph[x][y] = min(graph[x][y], graph[x][k] + graph[k][y])

    print(graph)
    print(f'#{tc}')