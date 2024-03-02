import itertools


def solution(orders, course):
    answer = []

    # orders를 배열 형태로 초기화
    new_orders = [[] for _ in range(len(orders))]
    for i in range(len(orders)):
        for menu in orders[i]:
            new_orders[i].append(menu)

    # 각 손님이 주문한 메뉴의 조합 생성 후 combs에 해당 조합이 나오는 횟수 저장
    combs = {}
    for order in new_orders:
        order.sort()
        for n in range(2, len(order) + 1):
            for comb in list(itertools.combinations(order, n)):
                temp = ''.join(c for c in comb)
                if temp not in combs:
                    combs[temp] = 1
                else:
                    combs[temp] += 1

    # 손님이 주문한 메뉴의 조합을 주문 개수 오름차순으로 정렬
    combs = sorted(combs.items(), key = lambda x:len(x[0]))

    # course의 개수만큼 배열 생성 (2개 조합의 개수, 3개의 조합의 개수, 5개 조합의 개수 따로 저장하기 위해)
    comb_by_number = [[] for _ in range(len(course))]
    
    # comb_by_number 배열에 구하려는 조합의 개수에 맞게 저장
    idx = 0
    for key, value in combs:
        if len(key) == course[idx]:
            comb_by_number[idx].append((key, value))
        if len(key) > course[idx]:
            if idx == len(course) - 1:
                break
            else:
                idx += 1
                if len(key) == course[idx]:
                    comb_by_number[idx].append((key, value))

    # 각 조합의 개수의 최댓값인 경우 answer에 추가
    for comb in comb_by_number:
        if comb == [] or max([c[1] for c in comb]) < 2:
            continue

        max_value = max([c[1] for c in comb])
        for key, value in comb:
            if value == max_value:
                answer.append(key)

    return sorted(answer)