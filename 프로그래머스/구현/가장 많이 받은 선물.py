def solution(friends, gifts):
    n = len(friends)

    # 친구 이름 딕셔너리화
    friends_dict = {}
    for i in range(len(friends)):
        friends_dict[friends[i]] = i

    # 각각 주고받은 선물의 수 구하기
    give_and_take = [[0 for _ in range(n)] for _ in range(n)]
    for gift in gifts:
        from_who, to_whom = gift.split()
        give_and_take[friends_dict[from_who]][friends_dict[to_whom]] += 1

    # 선물 지수 구하기
    present_factor = {i:0 for i in range(n)}
    for i in range(n):
        present_factor[i] = sum(give_and_take[i]) - sum([g[i] for g in give_and_take])

    # 누가 선물을 받는 지 계산
    next_get = {i:0 for i in range(n)}
    for i in range(n):
        for j in range(i + 1, n):
            if give_and_take[i][j] > give_and_take[j][i]:
                next_get[i] += 1
            elif give_and_take[i][j] < give_and_take[j][i]:
                next_get[j] += 1
            else:
                if present_factor[i] > present_factor[j]:
                    next_get[i] += 1
                elif present_factor[i] < present_factor[j]:
                    next_get[j] += 1

    return max(next_get.values())