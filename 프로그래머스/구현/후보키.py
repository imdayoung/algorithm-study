from itertools import combinations


def solution(relation):
    column = len(relation[0])
    row = len(relation)

    # 후보키
    combs = []
    for count in range(1, column + 1):
        combs.extend(list(combinations(range(column), count)))

    # 유일성 확인
    answer = []
    for comb in combs:
        temp = [tuple([l[i] for i in comb]) for l in relation]
        if len(set(temp)) == row:
            # 최소성 확인
            for a in answer:
                if set(a).issubset(set(comb)):
                    break
            else:
                answer.append(comb)
    
    return len(answer)