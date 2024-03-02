def palindrome(l):
    for i in range(N):
        temp = graph_r[i]
        for j in range(N - l):
            if temp[j] == temp[j + l]:
                if temp[j:j + l + 1] == temp[j:j + l + 1][::-1]:
                    return True

    for i in range(N):
        temp = graph_c[i]
        for j in range(N - l):
            if temp[j] == temp[j + l]:
                if temp[j:j + l + 1] == temp[j:j + l + 1][::-1]:
                    return True
                
    return False

T = 10
N = 100
for _ in range(1, T + 1):
    tc = int(input())
    
    graph_r, graph_c = [], []
    for _ in range(N):
        graph_r.append(list(map(str, input())))

    for i in range(N):
        graph_c.append([g[i] for g in graph_r])

    # print("-------------- 원본 그래프 --------------")
    # for g in graph_r:
    #     print(g)
    # print("-----------------------------------------")
    # print("-------------- 전환 그래프 --------------")
    # for g in graph_c:
    #     print(g)
    # print("-----------------------------------------")

    for i in range(N, 0, -1):
        if palindrome(i):
            print(f"#{tc} {i + 1}")
            break