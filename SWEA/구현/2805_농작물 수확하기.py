T = int(input())
for tc in range(1, T + 1):
    income = 0
    N = int(input())
    graph = []
    for _ in range(N):
        temp = list(map(int, input()))
        graph.append(temp)

    standard = N // 2
    for i in range(N):
        if i <= standard:
            income += sum(graph[i][standard - i:standard + i + 1])
        else:
            income += sum(graph[i][i - standard:standard - i])

    print(f'#{tc} {income}')
