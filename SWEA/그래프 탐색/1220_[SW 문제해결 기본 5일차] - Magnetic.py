T = 10
for tc in range(1, T + 1):
    graph = []
    N = int(input())
    for _ in range(N):
        graph.append(list(map(int, input().split())))

    # 테이블 아래로 떨어지는 자성체 걸러내기
    res = []
    for i in range(N):
        temp = [g[i] for g in graph]
        for i in range(len(temp)):
            # N극 자기장 가장 근처 자성체가 N극이면 더 이상 떨어지지 않음
            if temp[i] == 1:
                break
            # N극 자기장 가장 근처 자성체가 S극이면 테이블 아래로 떨어짐
            if temp[i] == 2:
                temp[i] = 0
        for i in range(len(temp) - 1, -1, -1):
            # S극 자기장 가장 근처 자성체가 S극이면 더 이상 떨어지지 않음
            if temp[i] == 2:
                break
            # S극 자기장 가장 근처 자성체가 N극이면 테이블 아래로 떨어짐
            if temp[i] == 1:
                temp[i] = 0
        res.append(temp)

    ans = 0
    for r in res:
        temp = ""
        for i in range(N):
            if r[i] != 0:
                temp += str(r[i])
        ans += temp.count("12")
    print(f"#{tc} {ans}")