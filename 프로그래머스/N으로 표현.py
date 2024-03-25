# 46M
def solution(N, number):
    answer = -1

    if number == N:
        return 1
    
    max_use = 8
    combs = [set() for _ in range(max_use + 1)]
    combs[1].add(N)

    # i개의 N으로 표현가능한 수 구하기
    for i in range(2, max_use + 1):
        # NNN으로 표현
        temp_add = int(str(N) * i)
        if number == temp_add:
            return i
        combs[i].add(temp_add)

        for j in combs[i - 1]:
            temp_plus = j + N
            temp_minus = j - N
            temp_mul = j * N
            temp_div = j // N

            if number in [temp_plus, temp_minus, temp_mul, temp_div]:
                return i
            
            combs[i].add(temp_plus)
            if temp_minus > 0: combs[i].add(temp_minus)
            combs[i].add(temp_mul)
            combs[i].add(temp_div)
        # print(combs[i])

    return answer


print(solution(5, 12))
# 4
print(solution(2, 11))
# 3