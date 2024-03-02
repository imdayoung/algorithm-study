def check_space(g):
    global answer
    for i in range(N):
        count = 0
        for j in range(N):
            if g[i][j] == 1:
                count += 1
            elif g[i][j] == 0:
                if count == K:
                    answer += 1
                count = 0

            if j == N - 1:
                if count == K:
                    answer += 1

T = int(input())
for tc in  range(1, T + 1):
    answer = 0

    N, K = map(int, input().split())
    graph_r = [list(map(int, input().split())) for _ in range(N)]
    graph_c = [[g[i] for g in graph_r] for i in range(N)]

    check_space(graph_r)
    check_space(graph_c)
    print(f"#{tc} {answer}")