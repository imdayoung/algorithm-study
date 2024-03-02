def ladder_ride(x, y):
    length = 1
    while x < 100:
        # 오른쪽으로 길이 있는 경우
        if y + 1 < 100 and graph[x][y + 1] == 1:
            while y + 1 < 100 and graph[x][y + 1] == 1:
                y += 1
                length += 1
            x += 1
            length += 1
        # 왼쪽 길이 있는 경우
        elif y - 1 > -1 and graph[x][y - 1] == 1:
            while y - 1 > -1 and graph[x][y - 1] == 1:
                y -= 1
                length += 1
            x += 1
            length += 1
        # 밑으로만 길이 있는 경우
        else:
            x += 1
            length += 1
    return length

T = 10
for _ in range(1, T + 1):
    answer = 0
    min_value = 10000

    start = []
    graph = []

    tc = int(input())
    temp = list(map(int, input().split()))
    graph.append(temp)
    for j in range(100):
        if temp[j] == 1:
            start.append((0, j))

    for _ in range(99):
        temp = list(map(int, input().split()))
        graph.append(temp)
    
    for x, y in start:
        temp = ladder_ride(x, y)
        if temp < min_value:
            min_value = temp
            answer = y

    print(f"#{tc} {answer}")