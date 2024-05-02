def solution(routes):
    answer = 0
    routes.sort(key = lambda x:(x[1], x[0]))

    point = -30001
    for i in range(len(routes)):
        # 새로운 카메라를 설치해야 하는 상황
        if routes[i][0] > point:
            answer += 1
            point = routes[i][1]

    return answer