for tc in range(1, 11):
    answer = 0

    graph = []
    graph_2 = []
    length = int(input())
    for _ in range(8):
        graph.append(list(map(str, input())))

    for i in range(8):
        for j in range(8 - length + 1):
            temp = graph[i][j:j + length]
            if temp == temp[::-1]:
                answer += 1

    for i in range(8):
        graph_2.append([g[i] for g in graph])

    for i in range(8):
        for j in range(8 - length + 1):
            temp = graph_2[i][j:j + length]
            if temp == temp[::-1]:
                answer += 1


    print(f'#{tc} {answer}')