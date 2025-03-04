def solution(park, routes):
    park_list = [[0 for _ in range(len(park[0]))] for _ in range(len(park))]
    i, j = 0, 0
    
    # 2차원 리스트로 만들기
    for p in park:
        for c in p:
            park_list[i][j] = c
            j += 1
        i += 1
        j = 0
    
    # S의 좌표 찾기
    for i in range(len(park)):
        for j in range(len(park[0])):
            if park_list[i][j] == "S":
                now_x = i
                now_y = j
                break
                
    for r in routes:
        direction, distance = r.split()[0], int(r.split()[1])
        if direction == "N" and now_x - distance >= 0:
            if "X" not in [i[now_y] for i in park_list][now_x - distance:now_x]:
                now_x -= distance
        elif direction == "S" and now_x + distance < len(park):
            if "X" not in [i[now_y] for i in park_list][now_x:now_x + distance + 1]:
                now_x += distance
        elif direction == "W" and now_y - distance >= 0:
            if "X" not in park_list[now_x][now_y - distance:now_y]:
                now_y -= distance
        elif direction == "E" and now_y + distance < len(park[0]):
            if "X" not in park_list[now_x][now_y:now_y + distance + 1]:
                now_y += distance

    return [now_x, now_y]