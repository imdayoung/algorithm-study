T = int(input())
for tc in range(1, T + 1):
    answer = 1
    check = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    graph_r = [list(map(int, input().split())) for _ in range(9)]
    graph_c = [[g[i] for g in graph_r] for i in range(9)]

    # 가로로 확인
    for g in graph_r:
        temp = g.copy()
        temp.sort()
        if temp != check:
            answer = 0
            break

    # 세로로 확인
    if answer == 1:
        for g in graph_c:
            temp = g.copy()
            temp.sort()
            if temp != check:
                answer = 0
                break

    # 칸 안 확인
    if answer == 1:
        for i in range(0, 7, 3):
            for j in range(0, 7, 3):
                temp = []
                temp.extend([graph_r[i][j], graph_r[i][j + 1], graph_r[i][j + 2]])
                temp.extend([graph_r[i + 1][j], graph_r[i + 1][j + 1], graph_r[i + 1][j + 2]])
                temp.extend([graph_r[i + 2][j], graph_r[i + 2][j + 1], graph_r[i + 2][j + 2]])
                temp.sort()
                if temp != check:
                    answer = 0
                    break
            if answer == 0:
                break

    print(f"#{tc} {answer}")